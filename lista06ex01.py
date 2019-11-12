ordem = 4
matriz = []
cont = 0
for i in range (ordem):
    matriz.append([0] * ordem)
for i in range (ordem):
    for j in range (ordem):
        matriz[i][j] = int(input('Digite um número para posição [' + str(i+1) + '][' + str(j+1) +']:'))
        if matriz[i][j] > 10:
            cont += 1
print ('A matriz possui {} valores acima de 10.'.format(cont))
