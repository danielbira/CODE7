'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
contrário, ele será classificado como "Inocente".'''

res = []

res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))

somaresposta = 0
for i in res:
	somaresposta += int(i)

print ('--------------')
if (somaresposta < 2):
 print("Inocente")
elif (somaresposta == 2):
 print("Suspeita")
elif (3 <= somaresposta <= 4):
 print("Cúmplice")
elif (somaresposta == 5):
 print("Assassino")
