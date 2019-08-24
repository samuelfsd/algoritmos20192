comprimento = float(input ('Informe o valor do comprimento da sala: '))
largura = float(input ('Informe o valor da largura da sala: '))
espprof = 1.5
spccadeira = comprimento - espprof
comprimento2 = float(input ('Informe o valor do comprimento da mesa: '))
largura2 = float(input ('Informe o valor da largura da mesa: '))
comprimento3 = 0.2
largura3 = 0.5
comprimento2 = comprimento2 + comprimento3
largura2 = largura2 + largura3
qntdfileiras = largura // largura2
qntdcadfila = spccadeira // comprimento2
qntdtotalcad = qntdfileiras * qntdcadfila
print ('Você terá nesse espaço uma quantidade de', qntdtotalcad,' cadeiras.')
