nova = input('Nova compra: ')
soma = 0
soma2 = 0
while nova != 'Não':
    produto = input ('Informe o produto: ')
    custo = float(input('Informe o preço: '))
    nova = input('Mais produtos (Sim/Não): ')
    soma += custo
print ('Total da compra: ',soma)
fechar = input('Deseja fechar o caixa: (Sim/Não)')
if fechar == 'Não':
    nova2 = input('Outra compra: ')
    while nova2 != 'Não':
        produto = input ('Informe o produto: ')
        custo2 = float(input('Informe o preço: '))
        nova2 = input('Mais produtos: (Sim/Não) ')
        soma2 += custo2
        fechar = input('Deseja fechar o caixa: (Sim/Não)')
print ('O total apurado foi :', soma + soma2)
    

