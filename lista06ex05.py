ordem = int(input('Informe a ordem da matriz: '))
matriz = []
soma = 0
aux = 0
for i in range (ordem):
    matriz.append([0]*ordem)
for i in range (ordem):
    for j in range (ordem):
        matriz[i][j] = int(input('Informe um número para a posição [{}][{}]: '.format(i+1, j+1)))#aplicando uma nova forma de mudar para o usuário e ficar [1][1]
for i in range (ordem - 1):
    for j in range (i+1, ordem):
        aux = matriz[i][j]
        soma += aux
print ('A soma dos números que estão acima da diagonal principal é {}'.format(soma))



