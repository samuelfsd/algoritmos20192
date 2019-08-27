horas = float(input('Informe as suas horas trabalhadas: '))
dinheirohora = float(input('informe o valor da hora: '))
salariofinal = horas * dinheirohora
ir = (5 / 100) * salariofinal
inss = (10 / 100) * salariofinal
fgts = (11 / 100) * salariofinal
vinte = (20 / 100) * salariofinal
if salariofinal <= 900:
    print ('Salário bruto é de: R$', salariofinal)
    print ('(-) IR (0%): R$ 0')
    print ('(-) INSS (10%): R$', inss)
    print ('FGTS (11%): R$', fgts)
    print ('Total de descontos: R$', inss)
    print ('Salário Líquido: R$', salariofinal - inss)
elif salariofinal > 900 and salariofinal <= 1500:
    print ('Salário bruto é de: R$', salariofinal)
    print ('(-) IR (5%): R$ ', ir)
    print ('(-) INSS (10%): R$', inss)
    print ('FGTS (11%): R$', fgts)
    print ('Total de descontos: R$', ir + inss)
    print ('Salário Líquido: R$', salariofinal -(ir + inss))
elif salariofinal > 1500 and salariofinal <= 2500:
    print ('Salário bruto é de: R$', salariofinal)
    print ('(-) IR (10%): R$ ', inss)
    print ('(-) INSS (10%): R$', inss)
    print ('FGTS (11%): R$', fgts)
    print ('Total de descontos: R$', inss + inss)
    print ('Salário Líquido: R$', salariofinal -(inss + inss))
else:
    print ('Salário bruto é de: R$', salariofinal)
    print ('(-) IR (20%): R$ ', vinte)
    print ('(-) INSS (10%): R$', inss)
    print ('FGTS (11%): R$', fgts)
    print ('Total de descontos: R$', vinte + inss)
    print ('Salário Líquido: R$', salariofinal -(vinte + inss))
