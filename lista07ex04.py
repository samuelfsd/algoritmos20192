def vetor_inteiros(x,n):
    for i in range (n):
        lista[i] = int(input('Informe um número: \n'))
def verifica_ordem(x,n):
    for i in range (n-1):
        if x[i] > x[i+1]:
            return False
    return True
n = int(input('Informe a quantidade de números inteiros: \n '))
lista  = [0]*n
vetor_inteiros(lista,n)
if verifica_ordem(lista,n):
    print ('Está em sequência.')
else:
    print('Não está em sequência.')