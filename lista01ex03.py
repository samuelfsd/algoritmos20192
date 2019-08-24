valor = float (input (' Informe o valor da dívida: '))
dias = float (input (' Quantos dias em atraso? '))
juros = float (input (' Informe o valor dos juros: '))
multa = float(dias*juros) + valor
print (' O valor da multa será de {:.2f}'.format (multa),'reais.')
