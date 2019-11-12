ordem = 10
matriz = [] 
for i in range (ordem):
    matriz.append([0] * ordem)
for i in range (ordem):
    for j in range (ordem):
        if i < j:
            matriz[i][j] = 2*i + 7*j - 2
        elif i > j:
            matriz[i][j] = 4*(i**3) - 5*(j**2) + 1
        elif i == j: 
            matriz[i][j] = 3*(i**2) - 1
#A matriz vai ser gerada pelas formulas ditas em cima
for i in range (ordem):
    print (matriz[i])
    
