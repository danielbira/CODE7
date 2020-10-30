'''Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''


temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = 0
acimaMedia = {}

for i in range(len(meses)):
	temperatura.append(float(input(f'Informe a temperatura média do mês ' + meses[i] + ': ')))
	media += temperatura[i]

for i in range(len(meses)):
	if temperatura[i] > media:
		acimaMedia = temperatura


print(f'A media das temperaturas dos mês {meses} é {temperatura}')
