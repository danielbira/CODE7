'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e informe
ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.'''

maior = menor = soma = quant = media = 0  
resp = "S"

while resp in "Ss":
	temperatura = float(input("Digite a temperatura: "))
	soma += temperatura
	quant += 1
	if quant == 1:
		maior = menor = temperatura
	else:
		if temperatura > maior:
			maior = temperatura
		if temperatura < menor:
			menor = temperatura

	resp = str(input("Queres continuar [S/N]: "))

media = soma/quant
print (f"A temperatura maior é: {maior}º")
print (f"A temperatura menor é: {menor}º")
print (f"A média das temperaturas é de: {media}º")