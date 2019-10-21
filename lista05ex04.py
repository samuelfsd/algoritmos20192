a = [0]*10
maior = 0
x = 0
for i in range (10):
    a[i] = int(input('Informe um número: '))
    if a[i] > maior:
        maior = a[i]
        x = i
print (a)
print ('O maior elemento é :',maior,'e ele está no índice',x,'.')



    
