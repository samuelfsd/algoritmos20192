ano = int(input('Informe o valor equivalente a um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano', ano,'é bissexto.')
else:
    print('O ano', ano,'não é bissexto.')
