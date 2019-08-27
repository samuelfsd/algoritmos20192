p1 = float(input('Informe o preço do primeiro produto: '))
p2 = float(input('Informe o preço do segundo produto: '))
p3 = float(input('informe o preço do terceiro produto: '))
if p1 < p2 < p3:
    print ('Deve-se comprar o primeiro produto já que está mais barato que os demais.')
elif p2 < p1 < p3:
    print ('Deve-se comprar o segundo produto já que está mais barato que os demais.')
else:
    print ('Deve-se comprar o terceiro produto já que está mais barato que os demais.')

    
    
