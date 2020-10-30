'''Exercício 01
Escrever um programa, que recebe os coeficientes (a, b, c) de uma equação de segundo grau, e
retorna o valor de Δ (delta). Utilizar a fórmula abaixo.'''

a = int (input("Digite o seu valor de a: "))
b = int (input("Digite o seu valor de b: "))
c = int (input("Digite o seu valor de c: "))

delta = (b**2) - (4*a*c)

print("O resultada da equação Δ (delta) é :", delta)

