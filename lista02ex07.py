turno = str(input('Informe em que turno você estuda:(M) matutino, (V) Vespertino ou (N) Noturno: '))
if turno == 'M' or turno == 'm':
    print ('Bom dia!')
elif turno == 'V' or turno == 'v':
    print ('Boa tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa noite')
else:
    print('Valor inválido.')
