linhas = int(input('Quantas linhas do triâgulo de Pascal: '))
pascal = []
for i in range(linhas):
    pascal.append([0]*(i+1))
for i in range(linhas):
    pascal[i][0]=1
    pascal[i][i]=1
for linha_matriz in range(1,linhas,1):
    for coluna_matriz in range(2,linhas,1):
        if linha_matriz < coluna_matriz:
            pascal[coluna_matriz][linha_matriz] = pascal[coluna_matriz -1][linha_matriz] + pascal[coluna_matriz -1][linha_matriz -1]
for i in range(linhas):
    for j in range(linhas):
        if i >= j:
            print(pascal[i][j],end=' ')
    print()





