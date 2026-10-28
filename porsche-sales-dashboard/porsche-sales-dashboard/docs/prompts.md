# Briefing e refinamentos da IA

## Prompt consolidado de implementação

> A partir das colunas sanitizadas da base de 100 operações Porsche, crie uma dashboard em um único index.html, com HTML, CSS, JavaScript e dados embutidos. Não use bibliotecas, fontes ou serviços externos. A interface deve ser em português, mantendo preços na moeda original USD.
>
> Responda três perguntas: (1) quais famílias geram mais receita, com barras de soma dos preços; (2) quais estados americanos concentram mais vendas, com barras de quantidade; (3) quais formas de pagamento são mais frequentes, com gráfico de rosca e legenda com contagem e percentual.
>
> Inclua KPIs de valor das operações, quantidade, ticket médio e família líder; filtros combináveis de família, modelo, estado, ano do veículo e pagamento; reset; tabela paginada; busca e exportação CSV do recorte. O filtro de modelos deve acompanhar a família selecionada. Ofereça um exemplo de filtro Califórnia.
>
> Use fundo marfim, verde escuro, sálvia e detalhes dourados. Combine tipografia sans-serif do sistema e um acento serifado no título. Layout responsivo, navegação por teclado e estado vazio sem erros.
>
> Exclua canceladas por padrão, mas permita incluí-las. Retenha os registros com data INVALID como data nula e informe a contagem. Não impute datas. Ano do modelo não é ano da venda. Receita é soma dos preços, não receita reconhecida. Remova nomes de clientes e vendedores de todos os arquivos públicos. Documente as regras e teste os totais antes da publicação.

Este texto consolida o briefing usado nesta sessão; não é uma transcrição de um prompt enviado ao Canvas ou a um agente externo. A implementação ocorreu diretamente no ChatGPT Work, com assistência de IA, leitura da planilha e orientações das skills de planilhas e Sites.

## Decisões e evolução até a versão final

1. Inspeção do anexo: o nome terminava em `.csv`, mas a assinatura interna era XLSX. A extração passou a reconhecer o formato real, sem usar a extensão como verdade.
2. Perguntas escolhidas antes da interface: mix de famílias, mercados por estado e pagamento. A família agrupa variantes para tornar a comparação legível.
3. A análise encontrou 7 canceladas e 24 datas inválidas. Foi adicionado o controle de canceladas e uma explicação do denominador e das datas.
4. USD foi mantido explicitamente; o idioma português não justifica conversão para BRL.
5. Busca foi limitada à tabela e à exportação, com explicação na interface. Os cinco filtros superiores atualizam todos os indicadores.
6. Testes no navegador cobriram filtro de Califórnia, combinação sem resultados, total incluindo canceladas, tabela e exportação. A redação da liderança por estado foi ajustada para distinguir um líder de empates.

## Para praticar uma segunda abordagem

O arquivo `data/sales.csv` permite comparar esta implementação com Canvas ou um agente com skill própria. Esse segundo experimento **não foi executado** nesta entrega. Para estudar, substitua a pergunta geográfica por ticket médio por estado e compare se o ranking muda; registre seu próprio prompt e suas decisões ao fazer essa alteração.
