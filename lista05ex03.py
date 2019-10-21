a = [0]*10
x = 0
for i in range (10):
    a[i] = int(input('Informe um número: '))
    if a[i] % 2 == 0:
        x += 1
print ('O arranjo possui',x,'valores pares.')
    


