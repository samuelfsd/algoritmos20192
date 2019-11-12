linhas = 3
colunas = 6 
matriz = []
soma = 0
media = 0
for i in range (linhas):
    matriz.append([0] * colunas)
for i in range (linhas):
    for j in range (colunas):
        matriz[i][j] =  int(input('Informe um número para a posição [{}][{}]: '.format(i+1,j+1)))
for i in range (linhas):
    for j in range (0,colunas,2):
            soma = soma + matriz[i][j]
print('A soma dos elementos das colunas ímpares',soma)
soma = 0
for i in range (linhas):
    soma = soma + matriz[i][1] + matriz[i][3]
media = soma / 6
print ('A média aritmética dos elementos da 2 e 4 colunas',media)
soma = 0
for i in range (linhas):
    soma = soma + matriz[i][0] + matriz[i][1]
    matriz[i][5] = soma
    soma = 0
print ('Essa é a Matriz modificada :)')
for i in range (linhas):
    for j in range (colunas):
        print (matriz[i][j], end= ' ')
    print ()
#se cair uma questão assim na prova eu só faço metade pq demorei umas 2 horas pra responder 
