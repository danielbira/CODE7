'''Escreva um código para remover valores duplicados da seguinte
lista:

notas = [7, 7, 5, 2, 8, 10, 8, 7, 3, 3, 10, 2, 5, 10, 5 ]'''

lista = [7, 7, 5, 2, 8, 10, 8, 7, 3, 3, 10, 2, 5, 10, 5 ]

remover = list(set(lista))

print(remover)