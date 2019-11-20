def vetor(tam):
    lista = [0]*tam
    for i in range (tam):
        lista[i] = int(input('Informe um número: \n'))
    return lista
def par(p,tam):
    par = []
    for i in range(tam):
        if p[i] % 2 == 0:
            par.append(p[i])
    return par
def imp(x,tam):
    imp = []
    for i in range (tam):
        if x[i] % 2 != 0:
            imp.append(x[i])
    return imp
tam = int(input('Informe o tamanho do vetor: \n'))
vetor = vetor(tam)
par = par(vetor,tam)
imp = imp(vetor,tam)
print (f'A lista de pares é:\n {par}')
print (f'A lista de ímpares é:\n {imp}')

