a = [0]*10
b = [0]*10
for i in range (10):
    a[i] = int(input('Informe um número: '))
    b[i] = a[i]
print (a)
print (b[::-1])

