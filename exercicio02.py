'''Escrever um programa, o qual recebe as medidas de dois catetos de um triângulo e retorna a
medida da hipotenusa do mesmo. Utilizar o Teorema de Pitágoras. '''

catopo = float (input("Digite o seu valor do cateto oposto: "))
catadj = float (input("Digite o seu valor do cateto adjacente: "))

hipotenusa = (catopo**2 + catadj**2) **(1/2)

print("o valor da Hipotenusa é: %.2f"  % hipotenusa)