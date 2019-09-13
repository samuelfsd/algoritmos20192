salario = float (input ('Informe o seu salário: '))
despesas = float (input ('Informe suas despesas mensais: '))
resto = salario - despesas
anos = 1000000 / (resto * 12) #anos = (1000000 / resto) * 12
print ('Você poupará 1,000,000 em {:.2f}'.format (anos), 'anos.')

                 
