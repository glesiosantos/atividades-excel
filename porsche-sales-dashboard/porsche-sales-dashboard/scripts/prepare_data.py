"""Extract sanitized values from the challenge XLSX, regardless of extension.
Usage: python scripts/prepare_data.py PATH_TO_ORIGINAL_FILE
Only the standard library is required. Never publishes customer/salesperson names.
"""
import csv
import datetime
import io
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def extract(path):
    if not zipfile.is_zipfile(path):
        with open(path, encoding='utf-8-sig', newline='') as stream:
            sample = stream.read(4096)
            stream.seek(0)
            return list(csv.DictReader(stream, dialect=csv.Sniffer().sniff(sample)))
    with zipfile.ZipFile(path) as archive:
        shared = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            shared = [''.join(si.itertext()) for si in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
        sheet = ET.fromstring(archive.read('xl/worksheets/sheet1.xml'))
        rows = []
        for row in sheet.findall('.//m:row', NS):
            values = {}
            for cell in row:
                col = re.sub(r'\d', '', cell.attrib['r'])
                if cell.find('m:f', NS) is not None:
                    raise ValueError(f'Formula found at {cell.attrib["r"]}; export values first')
                if cell.attrib.get('t') == 'inlineStr':
                    value = ''.join(cell.find('m:is', NS).itertext())
                else:
                    value = cell.findtext('m:v', '', NS)
                    if cell.attrib.get('t') == 's':
                        value = shared[int(value)]
                values[col] = value
            rows.append(values)
        headers = rows[0]
        return [{headers[col]: row.get(col, '') for col in headers} for row in rows[1:] if any(row.values())]


def prepare(path):
    output = []
    for row in extract(path):
        date = row['SaleDateSanitized'].strip()
        if date in ('', 'INVALID'):
            date = None
        else:
            datetime.date.fromisoformat(date)
        model = row['PorscheModelSanitized'].strip()
        family = next((name for name in ['718', '911', 'Cayenne', 'Macan', 'Panamera', 'Taycan'] if model.startswith(name)), 'Other')
        item = dict(id=int(row['sale_id']), date=date, model=model, family=family,
                    year=int(row['ModelYearSanitized']), price=float(row['SalesPriceSanitized']),
                    mileage=int(row['VehicleMileageSanitized']), payment=row['PayMethodSanitized'].strip(),
                    city=row['CitySanitized'].strip(), state=row['StateSanitized'].strip(),
                    status=row['DeliveryStatusSanitized'].strip())
        assert item['price'] > 0 and 1900 <= item['year'] <= 2100
        assert re.fullmatch(r'[A-Z]{2}', item['state'])
        assert item['family'] != 'Other'
        output.append(item)
    assert len({r['id'] for r in output}) == len(output), 'Duplicate sale IDs'
    (ROOT / 'data').mkdir(exist_ok=True)
    (ROOT / 'data/sales.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    with (ROOT / 'data/sales.csv').open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)
    html = ROOT / 'index.html'
    if html.exists():
        content = html.read_text()
        content = re.sub(r'(<script id="sales-data" type="application/json">).*?(</script>)',
                         lambda m: m[1] + json.dumps(output, ensure_ascii=False).replace('<', '\\u003c') + m[2],
                         content, flags=re.S)
        html.write_text(content)
    active = [r for r in output if r['status'] != 'Cancelled']
    print(json.dumps(dict(rows=len(output), invalid_dates=sum(r['date'] is None for r in output),
                          cancelled=len(output)-len(active), active_revenue=round(sum(r['price'] for r in active), 2),
                          active_count=len(active), all_revenue=round(sum(r['price'] for r in output), 2)), indent=2))


if __name__ == '__main__':
    prepare(sys.argv[1])
