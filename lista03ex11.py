num = int(input('Informe um número: '))
soma = 0
soma = soma + num
n = 1
par = 0
imp = 0
while n < 10:
    num = int(input('Informe um número: '))
    soma = soma + num
    n += 1
    if num % 2 == 0:
        par += 1
    else:
        imp += 1
print (soma)
print('A quantidade de números pares é: ', par)
print('A quantidade de números ímpares é: ', imp) 
