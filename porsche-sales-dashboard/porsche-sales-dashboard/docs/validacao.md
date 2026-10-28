# Evidências e validação

## Conferência independente dos totais

Valores calculados a partir dos registros, com conferência decimal no script `scripts/validate.py`:

| Cenário | Operações | Valor das operações (USD) |
|---|---:|---:|
| Base completa, incluindo canceladas | 100 | 12.827.800,50 |
| Padrão, excluindo canceladas | 93 | 12.202.550,50 |
| Califórnia (CA), excluindo canceladas | 16 | 1.973.350,00 |

No recorte padrão, a família 911 soma USD 4.168.100,00 (34,2%); a Califórnia lidera com 16 operações; Wire Transfer tem 26 operações (28,0%). O ticket médio é USD 131.210,22 (arredondado aos centavos). São 23 datas inválidas no recorte padrão e 24 na base completa.

## Verificações no navegador

- Carregamento inicial, gráficos e KPIs: conferidos com os totais acima.
- Botão “Explorar Califórnia”: 16 operações e USD 1.973.350,00.
- Combinação CA + família 911 + pagamento Cash: estado vazio, com zero operações, sem NaN/Infinity.
- Limpar filtros e incluir canceladas: 100 operações e USD 12.827.800,50.
- Tabela, busca, paginação e exportação CSV: verificadas na prévia local.
- Console da página: sem erro de aplicação encontrado. Mensagens da extensão do navegador não fazem parte do código do painel.

Capturas reais da prévia: `dashboard.jpg` e `filtro-california.jpg`. Os testes da prévia não certificam a publicação no GitHub Pages. Enquanto o endereço publicado não tiver sido confirmado, a implantação permanece pendente.
