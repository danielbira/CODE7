# Gostei da forma que você fez o tratamento de erros. Contudo, sugiro dividir 
# a única função em três funções: ler, validar, retornar. 
# Segue minha versão do código.

def recebe_int():
    # Recebe int
    numero = input('Digite um número inteiro: ')
    return numero

def valida_int(numero):
    # Valida int de entrada
    valida = False
    if numero.isnumeric():
        valida = True
    else:
        print("ERRO! Digite o número válido.")
    return valida

def retorna_int(numero):
    # Retorna int
    print(f'Você acabou de digitar o número inteiro {numero}.')

if __name__ == '__main__':
    # Main program
    while(True):
        numero = recebe_int()
        valida = valida_int(numero)
        if valida:
            retorna_int(numero)
