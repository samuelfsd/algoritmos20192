contagem = 0
entrada = str(input('Telefonou para a vítima? '))
if entrada == 'SIM' or entrada == 'sim' or entrada == 'Sim':
    contagem = contagem + 1
entrada = str(input('Esteve no local do crime? '))
if entrada == 'SIM' or entrada == 'Sim' or entrada == 'sim':
    contagem = contagem + 1
entrada = str(input('Mora perto da vítma? '))
if entrada == 'SIM' or entrada == 'Sim' or entrada == 'sim':
    contagem = contagem + 1
entrada = str(input('Devia para a vítma? '))
if entrada == 'SIM' or entrada == 'Sim' or entrada == 'sim':
    contagem = contagem + 1
entrada = str(input('Já trabalhou para a vitma? '))
if entrada == 'SIM' or entrada == 'Sim' or entrada == 'sim':
    contagem = contagem + 1
if contagem == 5:
     print('Assasino')
elif contagem >= 3 <= 4:
    print('Cúmplice.')
elif contagem == 2:
    print ('Suspeito.')
elif contagem >= 0 < 2:
    print('Inocente.')
