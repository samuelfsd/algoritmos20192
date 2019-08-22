valor = float (input ('Informe o valor do combustível: '))
dinheiro = float (input ('Quanto em dinheiro você quer gastar? '))
litros = (dinheiro/valor)
print ('Você tem {:.2f}'.format(litros),'litros em seu tanque.')
