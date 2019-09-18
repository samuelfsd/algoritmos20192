a = float(input('Informe o coeficiente da equação a= '))
if a == 0:
    print('Essa equação não é do segundo grau.')
else:
    b = float(input('Informe o valor da equação b= '))
    c = float(input('Informe o  valor da equação c= '))
    delta = b**2-4*a*c
    if delta < 0:
        print ('Essa equação não possui valores reais.')
    #Se você calcular a raiz de delta aqui o programa realizará o calculo mesmo que delta seja menor que zero, ocorrendo um erro
    raizdelta = delta ** 0.5
    x1 = (-b + raizdelta) / (2 * a)
    x2 = (-b - raizdelta) / (2 * a)
    if delta == 0:
        print('A equação só possui apenas uma raís. Que é:', x1)
    elif delta > 0:
        print('A equação possui 2 valores que são:', x1,'e', x2)
    

