a = [0]*10
valor = 0
for i in range (10):
    valor = int(input('Informe os números: '))
    a[i] = valor
for i in range (10):
    for j in range (i+1,10,1):
        if a[j] == a[i]:
            print ('O valor',a[i],'se repetiu!')

