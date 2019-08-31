numero = int(input('Qual valor você quer sacar: R$ '))
if numero // 100 != 0:
    a = numero // 100
    numero %= 100
    print(f'Total de {a} cédulas de R$100')
if numero // 50 != 0:
    a = numero // 50
    numero %= 50
    print(f'Total de {a} cédulas de R$50')
if numero // 10 != 0:
    a = numero // 10
    numero %= 10
    print(f'Total de {a} cédulas de R$10')
if numero != 0 and numero // 5 != 0:
    b = numero // 5
    numero %= 5
    print(f'Total de {b} cédulas de R$5')
if numero != 0:
    print(f'Total de {numero} cédulas de R$1')


