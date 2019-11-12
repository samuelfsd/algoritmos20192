ordem = int(input('Informe a ordem da matriz: '))
matriz = []
soma = 0
aux = 0
for i in range (ordem):
    matriz.append([0]*ordem)
for i in range (ordem):
    for j in range (ordem):
        matriz[i][j] = int(input('Informe um número para a posição [{}][{}]: '.format(i+1, j+1))) #continuo usando dessa forma pois está funcionando normal e reduz o tamanho do programa.
for j in range (ordem -  1):
    for i in range (j+1, ordem):
        aux = matriz[i][j]
        soma += aux
print ('A soma dos números abaixo da diagonal principal é {}'.format(soma))
