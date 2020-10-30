'''Qual Tipo do Triângulo?
Escreva um algoritmo que lê três medidas e verifica se elas formam um triângulo.
Caso positivo, o algoritmo deve identificar qual o tipo de triângulo formado: equilátero,
isósceles ou escaleno.

A saída deve estar no seguinte formato:
“As medidas Medida 1, Medida 2 e Medida 3 formam um triângulo <tipo do Triângulo>.”
Ou, no caso de não formar um triângulo:
“As medidas Medida 1, Medida 2 e Medida 3 não formam um triângulo.”.'''

a = float(input('Favor informe a medida 1: '))
b = float(input('Favor informe a medida 2: '))
c = float(input('Favor informe a medida 3: '))

if a < b + c and b < a + c and c < a + b:
		if a == b == c:
			print(f'As medidas Medida 1, Medida 2 e Medida 3, são iguais, pois formam um triângulo Equilátero.')
		elif a == b != c:
			print(f'As medidas Medida 1 e Medida 2 são iguais, por isso formam um triângulo Isósceles.')
		elif b == c != a:
			print(f'As medidas Medida e Medida 3 são iguais, por isso formam um triângulo Isósceles.')
		elif a == c != b:
			print(f'As medidas Medida 1 e Medida 3: são iguais, por isso formam um triângulo Isósceles.')
		else:
			print(f'As medidas Medida 1, Medida 2 e Medida 3 são diferentes, por isso formam um triângulo Escaleno.')
else:
	print(f'As medidas passadas não formam nenhum triângulo')