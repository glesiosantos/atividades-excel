"""Validate the deliverable without installing dependencies: python scripts/validate.py."""
import csv
import io
import json
import pathlib
import re
from decimal import Decimal

ROOT = pathlib.Path(__file__).resolve().parents[1]
html = (ROOT / 'index.html').read_text()
rows = json.loads((ROOT / 'data/sales.json').read_text())
embedded = json.loads(re.search(r'<script id="sales-data" type="application/json">(.*?)</script>', html, re.S)[1])
assert embedded == rows
assert len(rows) == 100
assert len({r['id'] for r in rows}) == 100
assert sum(r['date'] is None for r in rows) == 24
assert sum(r['status'] == 'Cancelled' for r in rows) == 7
assert all(isinstance(r['price'], (float, int)) and isinstance(r['year'], int) for r in rows)
assert len(list(csv.DictReader(io.StringIO((ROOT / 'data/sales.csv').read_text())))) == 100
assert not any(k in rows[0] for k in ['customer_name', 'salesperson'])
assert '<script src=' not in html and '<link rel="stylesheet"' not in html
amount = lambda rs: sum((Decimal(str(r['price'])) for r in rs), Decimal('0'))
active = [r for r in rows if r['status'] != 'Cancelled']
ca = [r for r in active if r['state'] == 'CA']
assert len(active) == 93 and amount(active) == Decimal('12202550.50')
assert amount(rows) == Decimal('12827800.50')
assert len(ca) == 16 and amount(ca) == Decimal('1973350.00')
assert amount([r for r in active if r['family'] == '911']) == Decimal('4168100')
assert sum(r['payment'] == 'Wire Transfer' for r in active) == 26
for path in ['docs/dashboard.jpg', 'docs/filtro-california.jpg', 'docs/prompts.md', 'docs/tratamento.md', 'docs/validacao.md', 'README.md']:
    assert (ROOT / path).stat().st_size > 0, f'Missing or empty: {path}'
for target in re.findall(r'\]\(([^)]+)\)', (ROOT / 'README.md').read_text()):
    if not target.startswith(('http:', 'https:', '#')):
        assert (ROOT / target).is_file(), f'Broken README link: {target}'
print('PASS: 100 rows; embedded JSON = public JSON; privacy fields removed; CSV; amounts; filters; README links; evidence files.')
