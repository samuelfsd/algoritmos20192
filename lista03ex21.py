n = int(input('Informe um número: '))
primo = 0
for i in range (2,n + 1,1):
    cont = 0
    for k in range (1, i+1,1):
        if i % k == 0:
            cont = cont + 1
    if cont <= 2:
        primo = i
        print(primo,end = ' ')
