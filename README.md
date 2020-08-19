# Trabalho Final da disciplina de Modelagem Baseada em Agentes (ABM) em Python do Mestrado do Ipea
### Sob orientação do Prof. Dr. Bernando Furtado

## Este trabalho procurou aplicar os conhecimentos adquiridos ao longo do curso, como funções, loops, condicionantes, operadores lógicos 
Professor Bernado, não é uma modelagem da realidade no nível de “Matrix” nem mesmo uma tentativa de previsão com base na psico-história de Isaac Asimov, mas é um começo em ABM ao tentar compreender/abstrair o comportamento de agentes em um processo de inflação (arbitrariamente estabelecida) com variação nas taxas de cheques especial quando o salário se mantém constante.
O resultado é uma quimera da segunda lista de exercícios com o seu exemplo de escolha de posto de combustível.

##	Quais são os agentes?

   Os agentes são os clientes que vão ao mercado comprar mantimentos.
As classes criadas foram pessoa, conta, mercado e compra, e a interação ocorre no módulo simulação.

##	Qual é o processo a se replicar?

Uma simulação de agente num processo de compra de mantimentos em mercados com bases em critérios de preferência e condições. 
Identificar o peso de diferentes taxas de cheque especial e da política de cash-back sobre o endividamento.
No arquivo gerado “preferências” é possível ver o qual o fator de preferência prevaleceu em cada rodada.
Os dados de cada simulação são salvos automaticamente no arquivo “simulação”, sendo sobrescrito a cada rodada.

##	Quais são as regras?

Cada simulação ocorre sobre 100 agentes com salário-mínimo fixo de R$1.045,00, num cenário de 20 mercados, com política de cash-back variando de 0 a 3% sobre o preço de produtos, e o custo destes produtos varia de 80 a 120% do salário-mínimo, assim, caso este custo supere o valor do salário, o agente entra no cheque especial, que possui taxas variando de 3%, 5% e 7% ao mesmo.

##	Qual é o ambiente e o processo?

Verificar a preferência do agente com base na distância do mercado, no valor dos mantimentos e na política de cash-back do mercado, bem como verificar o custo do cheque especial com diferentes taxas em um cenário de aumento no valor dos mantimentos acima do salário.

As ações ocorrem em um período único da seguinte forma: um agente com uma id possui uma conta, esta conta possui uma taxa de cheque especial variando randomicamente de 3%, 5% ou 7%, este agente recebe um salário fixo e com base no critério de preferência aleatoriamente escolhido se dirige até um mercado com uma id que possui o custo do mantimento variando aleatoriamente de 80 a 120% do salário do agente e uma política de cash-back  variando randomicamente de 0 a 3% do valor dos mantimentos.

## Como executar o programa
No módulo simulação é feita a escolha da quantidade de agentem e de mercados e do valor do salário.
Os resultados serão exibidos no console e os dados gerados serão salvos no arquivo simulacao.csv que será gerado na mesma pasta que encontram-se os programas.