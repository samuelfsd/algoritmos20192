def ler_matriz(linhas,colunas):
    matriz = []
    for i in range (linhas):
        matriz.append([0]*colunas)
    for i in range (linhas):
        for j in range (colunas):
            matriz[i][j] = int(input(f'Informe um elemento para a posição [{i+1}][{j+1}]'))
    return matriz
def verifica_mult(linhas,colunas,matriz,n):
    aux = 0
    for i in range (linhas):
        for j in range (colunas):
            if matriz[i][j] % n == 0:
                aux += 1
    return aux
linhas = int(input('Informe as linhas: ')) 
colunas = int(input('Informe as colunas: ')) 
n = int(input('Qual número você vai verificar: '))
matriz = ler_matriz(linhas,colunas)
multiplos = verifica_mult(linhas,colunas,matriz,n)
print ('O valor informado tem ',multiplos,'múltiplos nessa matriz.')