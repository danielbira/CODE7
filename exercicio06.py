'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências. Faça um programa que implemente
uma caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero
deve ser informado pelo operador para indicar o final da compra. O programa
deve então mostrar o total da compra e perguntar o valor em dinheiro que o
cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima
compra.'''

while (True):

	produto = 1
	total = 0
	valor = 1

	print (".............")
	print ("Loja Tabajara")
	print (".............")
	while valor != 0:
		valor = float(input(f"Digite o valor do produto {produto}: R$ "))
		produto += 1
		total += valor
		if valor == 0:
			break

	print (".............")
	print ("O valor Total: R$ {:.2f} ".format(total))
	print (".............")
	dinheiro = int(input("Digite o valor recebido: R$ "))
	troco = dinheiro - total
	print (".............")
	print ("Troco: R$ {:.2f}".format(troco))
