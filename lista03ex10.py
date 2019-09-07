base=int(input('Informe a base: '))
expoente=int(input('Informe o expoente: '))
pot = 1
c = 1
while c <= expoente:
    pot *= base
    c += 1
print(base,"^",expoente,"=",pot)
