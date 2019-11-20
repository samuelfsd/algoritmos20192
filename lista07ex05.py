def matriz(ordem,matriz_a,matriz_b):
    for i in range (ordem):
        matriz_a.append([0]*ordem)
        matriz_b.append([0]*ordem)
    for i in range (ordem):
        for j in range (ordem):
            matriz_a[i][j] = int(input(f'Informe a posição [{i+1}][{j+1}]:Matriz 1 \n '))
            matriz_b[i][j] = int(input(f'Informe a posição [{i+1}][{j+1}]:Matriz 2 \n '))
def troca_linha(matriz_a,matriz_b,l1,c1):
    aux = matriz_a[l1-1][c1-1]
    matriz_a[l1-1][c1-1] = matriz_b[l1-1][c1-1]
    matriz_b[l1-1][c1-1] = aux
matriz_a = []
matriz_b = []
ordem = int(input('Informe a ordem: '))
matriz(ordem,matriz_a,matriz_b)
print ('Matriz 1: ')
for i in range (ordem):
    print (matriz_a[i])
print('Matriz 2: ')
for i in range (ordem):
    print (matriz_b[i])
l1 = int(input('Linha: '))
c1 = int(input('Coluna: '))
troca_linha(matriz_a,matriz_b,l1,c1)
print ('Matriz 1:Depois da troca ')
for i in range (ordem):
    print (matriz_a[i])
print('Matriz 2:Depois da troca ')
for i in range (ordem):
    print (matriz_b[i])
