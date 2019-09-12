qnt = int(input('Digite a quantidade de CDs: '))
x = 0
total = 0
for i in range(qnt):
	cd = float(input('Digite o valor do CD: '))
	total = total + cd
	media = total / qnt
	x += 1
print('O valor total gasto: R$: ',total)
print('O valor médio gasto por cada CD foi de: R$:', media)
