qnt =  int(input('Quantos valores da sequencia Fibonacci: '))
ant = 1
atual = 1
print ('1 1', end = ' ')
cont = 2
while cont < qnt:
    prox = ant + atual
    ant = atual
    atual = prox
    print (prox, end = ' ')
    cont += 1
