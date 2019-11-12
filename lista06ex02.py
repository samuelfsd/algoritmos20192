ordem = 5
matriz = []
for i in range (ordem):
    matriz.append([0] * ordem)
for i in range (ordem):
    for j in range (ordem):
        matriz[i][j] = int(input('Informe um número para a posição [' + str (i+1) +'][' + str (j+1) + ']:'))
x = int(input('Informe um valor X para buscar na matriz um valor equivalente: '))
for i in range (ordem):
    for j in range (ordem):
        if matriz[i][j] == x:
            print ('Está na posição[' + str (i+1) +'][' + str (j+1) + ']:')
        elif matriz[i][j] == x:
            print ('Esse valor não foi encontrado na matriz.')