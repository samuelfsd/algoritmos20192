qnt = int(input('Digite a quantidade de numeros: '))
num = int(input('Digite o numero: '))
total = num
maior = num
menor = num
for i in range (1,qnt):
    num = int(input('Digite o numero: '))
    total = num + total
    if num < menor:
       menor = num
    if num > maior:
       maior = num
print('A soma é:' , total)
print('O menor numero é:' , menor)
print('O maior numero é' , maior)
#wtf n vi que estava sem nada 
