
'''
Faça um programa que leia nome e média de um aluno, guardando também a
situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

• Situação < 3: reprovado
• 3 < Situação < 7: recuperação
• Situação > 7: aprovado
'''


aluno = {}
aluno ['nome'] = str(input('Nome: '))
aluno ['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
	aluno['situacao'] = 'Aprovado'
elif 3 <= aluno['media'] < 7:
	aluno['situacao'] = 'Recuperação'
else:
	aluno['situacao'] = 'Reprovado'

print(f'A situação de {aluno["nome"]} é {aluno["situacao"]}, pois a média {aluno["media"]}. ')