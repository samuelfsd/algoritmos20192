def vetor(n):
    lista = [0]*n
    for i in range (n):
        lista[i] = int(input('Informe um número inteiro: '))
    return lista
def inversor(x):
    x.reverse()
    return x
n = int(input('Quantos elementos: '))
z = vetor(n)
print ('Esse é o vetor invertido \n ',inversor(z))

