ordem = 4
matriz_a = []
matriz_b = []
matriz_c = []
for i in range (ordem):
    matriz_a.append([0] * ordem)
    matriz_b.append([0] * ordem)
    matriz_c.append([0] * ordem)
for i in range (ordem):
    for j in range (ordem):
        matriz_a[i][j] = int(input('Informe um número para a posição [' + str (i+1) +'][' + str (j+1) + '] Da matriz 1:'))
for i in range (ordem):
    for j in range (ordem):
        matriz_b[i][j] = int(input('Informe um número para a posição [' + str (i+1) +'][' + str (j+1) + '] Da matriz 2:'))
for i in range (ordem):
    for j in range (ordem):
        if matriz_a[i][j] > matriz_b[i][j]:
            matriz_c[i][j] = matriz_a[i][j]
        else:
            matriz_c[i][j] = matriz_b[i][j]
print ('Uma terceira matriz com os maiores valores das duas anteriores: ')
for i in range (ordem):
    print (matriz_c[i])