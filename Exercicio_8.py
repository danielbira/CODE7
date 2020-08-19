'''lista = [5,3,2,4,7,1,0,6]'''

lista = []
for c in range(8):
    n = int(input('Digite o Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i,n)
                break
print ('A ordem crescente da lista é', (lista))