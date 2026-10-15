Simulador de renda com FIIs
Projeto de estudo em Excel para estimar o efeito de aportes mensais sobre o patrimônio e os dividendos projetados. Os valores de entrada e as alocações são exemplos fictícios.
Arquivos
- simulador_fii.xlsx: planilha editável com fórmulas, lista de perfis, cenários e gráfico de alocação.
- evidencias/simulacao-moderado.png e evidencias/simulacao-arrojado.png: a mesma simulação com dois perfis para demonstrar a mudança na divisão do aporte.
- evidencias/configuracoes.png: tabela de alocações usada pela busca.
Perguntas respondidas
Pergunta	Onde usar ou consultar
Quanto investir por mês?	Informe o aporte manual em Simulador!B5. A planilha também mostra uma sugestão de 30% do salário em Simulador!B10, calculada a partir de B9.
Por quantos anos?	Informe o prazo em Simulador!B6.
Qual a taxa de rendimento mensal?	Informe a taxa mensal em Simulador!B7.
Quanto de patrimônio vai acumular?	Consulte Simulador!E5 para o aporte informado e E11 para a sugestão de aporte. A tabela A14:C19 mostra projeções em 2, 5, 10, 20 e 30 anos.
Quanto vai receber de dividendos por mês?	Consulte Simulador!E6 para o aporte informado e E12 para a sugestão. A coluna C15:C19 exibe a projeção por prazo.


Na célula Simulador!B8, escolha Prudente, Moderado ou Arrojado. Isso atualiza o percentual e o valor mensal de cada tipo de fundo em F15:G20, além do gráfico de pizza. Os valores de G15:G20 totalizam o aporte em G21.
Como os cálculos funcionam
Patrimônio com VF / FV
O Excel em português apresenta a função como VF; o arquivo usa a forma interna FV, que representa a mesma função. Em Simulador!E5, a fórmula usa a taxa mensal, o número de meses (prazo × 12), o aporte mensal com sinal negativo para indicar saída de caixa, saldo inicial zero e pagamentos no fim do mês:
=FV(taxa_mensal,prazo_anos*12,-aporte,0,0)
O resultado é positivo porque a função retorna o valor acumulado. Os dividendos mensais estimados em E6 são o patrimônio acumulado multiplicado pela taxa mensal. A projeção de aporte sugerido usa o mesmo cálculo com aporte_sugerido.
Alocação com PROCV / VLOOKUP
Na aba Configuracoes, a coluna A cria uma chave composta pela junção do perfil e do tipo de fundo, como Moderado|Logística. Na aba Simulador, a fórmula procura a mesma chave e retorna a quarta coluna da tabela, o percentual:
=VLOOKUP($B$8&"|"&E15,Configuracoes!$A$4:$D$21,4,FALSE)
O último argumento (FALSE) exige correspondência exata. No Excel em português, a função é exibida como PROCV.
Intervalos nomeados
Nome	Referência
aporte	Simulador!$B$5
prazo_anos	Simulador!$B$6
taxa_mensal	Simulador!$B$7
perfil_investidor	Simulador!$B$8
salario_mensal	Simulador!$B$9
aporte_sugerido	Simulador!$B$10


Percentuais de exemplo
Perfil	Recebíveis (papel)	Logística	Lajes corporativas	Shoppings	Fundos de fundos	Desenvolvimento	Total
Prudente	35%	20%	10%	10%	15%	10%	100%
Moderado	25%	20%	15%	15%	15%	10%	100%
Arrojado	15%	20%	15%	20%	15%	15%	100%


Essas proporções foram definidas para este exercício e demonstram a validação do perfil e o uso de chave composta. Não vieram de uma fonte de mercado e não constituem recomendação de investimento. Os totais dos perfis são calculados na aba Configuracoes, coluna E.
Diferenças desta versão
- Layout organizado como um painel de uso, com entradas destacadas em amarelo e resultados calculados em cinza.
- Comparação entre o aporte digitado e a sugestão de 30% do salário.
- Gráfico de alocação que acompanha o perfil escolhido.
- Observações explícitas sobre hipóteses e limites da simulação.
- Cenários de patrimônio e dividendos para cinco prazos.
Premissas e limitações
- Aporte realizado ao fim de cada mês.
- Taxa mensal constante durante todo o prazo.
- A simulação não inclui impostos, taxas, vacância, mudanças de preço das cotas, reinvestimento separado de dividendos ou variação dos rendimentos.
- O valor de dividendos é uma estimativa matemática e não uma promessa de retorno.
- Salário, aporte, taxa, prazo e percentuais são exemplos. Substitua-os por valores adequados ao seu exercício.
