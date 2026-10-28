# Tratamento da base

Fonte primária deste projeto: anexo `base_vendas_porches.csv`, recebido no desafio DIO. Apesar do nome, é um arquivo XLSX (ZIP com XML de planilha), com 100 linhas de dados e identificadores de 6 a 105. Foram usados os valores sanitizados presentes nesse anexo; não foi substituído silenciosamente pela planilha disponível na URL do enunciado.

| Entrada | Saída pública | Regra |
|---|---|---|
| sale_id | id | Inteiro; chave técnica sem nome de pessoa |
| SaleDateSanitized | date | ISO YYYY-MM-DD; INVALID vira null |
| PorscheModelSanitized | model | Texto já normalizado |
| prefixo do modelo | family | 718, 911, Cayenne, Macan, Panamera ou Taycan |
| ModelYearSanitized | year | Inteiro; ano do veículo |
| SalesPriceSanitized | price | Número decimal, em USD; sem conversão cambial |
| VehicleMileageSanitized | mileage | Inteiro; mantida a unidade sanitizada de milhas |
| PayMethodSanitized | payment | Categoria original preservada |
| CitySanitized | city | Cidade sanitizada |
| StateSanitized | state | Sigla de estado dos EUA |
| DeliveryStatusSanitized | status | Categoria original preservada |
| customer_name, salesperson | removidos | Nenhum nome de cliente ou vendedor é publicado |
| demais colunas cruas | removidas | Apenas valores sanitizados alimentam o painel |

Os arquivos públicos JSON e CSV contêm somente esses 11 campos. As fórmulas são rejeitadas pelo extrator, para evitar resultados de fórmula quebrados. Neste anexo, as células utilizadas já continham valores.

## Inconsistências e limites

- 24 datas INVALID: mantidas como nulas, sem inferir datas a partir do dado cru. Contam nos totais e aparecem como “Sem data válida” na tabela.
- 7 cancelamentos: preservados na base e excluídos do recorte padrão. O usuário pode incluí-los explicitamente.
- Nem todo registro é uma entrega concluída. O total monetário representa valor das operações, não receita reconhecida, lucro ou caixa recebido.
- Datas de 2024 a 2027 pertencem à base educacional; não representam uma série histórica comercial verificada. Não se construiu gráfico temporal a partir delas.
- A quilometragem sanitizada foi preservada sem reinterpretar valores suspeitos. Esse campo não participa dos KPIs ou gráficos.
- Wire Transfer, Bank Transfer e ACH Payment continuam separados. Uma consolidação exigiria uma nova regra de negócio, não uma correção de texto.
- Não foram deduzidos imposto, margem, custos ou câmbio, pois não existem na base.
- Não há integração oficial com a Porsche. O material é um estudo, não um relatório da marca. Mesmo bases de estudo devem ser revistas antes de receber dados reais.

## Reprodução

Python 3, somente biblioteca padrão:

```bash
python scripts/prepare_data.py /caminho/para/o/anexo-original
python scripts/validate.py
```

O primeiro comando atualiza `data/sales.json`, `data/sales.csv` e os dados embutidos em `index.html`. O arquivo original deve ficar fora do repositório, pois contém nomes. O extrator também aceita CSV UTF-8 real com os cabeçalhos sanitizados originais. O validador fixa os números esperados deste desafio; ajuste essas expectativas conscientemente se trocar a base.
