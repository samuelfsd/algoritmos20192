maior = menor = cont = x = x1 = x2 = x3 = 0
cidmaior = ''
cidmenor = ''
for i in range (1,6,1):
    cidade = str(input('Informe o nome da cidade: '))
    codigo = int(input('Informe o código da cidade: '))
    veiculos = int(input('Informe o número de veiculos de passeio: '))
    acidentes = int(input('Informe o número de acidentes com vítmas: '))
    cont = cont + 1
    x = x + veiculos
    x1 = x / cont
    x2 += acidentes
    if acidentes > maior:
        maior = acidentes
        cidmaior = cidade
    if cont == 1 or acidentes < menor:
        menor = acidentes
        cidmenor = cidade
    if veiculos < 2000:
        x3 = x2 / cont
print ('O maior indice de acidentes de transito é', maior,',que é na cidade', cidmaior,'.')
print ('O menor indice de acidentes de transito é', menor,',que é na cidade', cidmenor,'.')
print ('A média de veiculos é',x1)
print ('A média de acidentes de transito nas cidades com menos de 2000 veiculos é',x3)
    
