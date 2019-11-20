def vetor_inteiros(tam):
    lista = [0]*tam
    for i in range (tam):
        lista[i] = int(input('Informe um número: \n'))
    return lista
def concatencao(tam_1,tam_2,lista_c,lista_a,lista_b):
    for i in range (tam_1+tam_2):
        if i < tam_1:
            lista_c[i] = lista_a[i]
        else:
            lista_c[i] = lista_b[i - tam_1]
    return lista_c
tam_1 = int(input('Informe o tamanho do vetor 1:\n '))
tam_2 = int(input('Informe o tamanho do vetor 2: \n'))
lista_a = vetor_inteiros(tam_1)
lista_b = vetor_inteiros(tam_2)
lista_c = [0]*(tam_1+tam_2) 
print ('Esse é o vetor concatenado: \n ',concatencao(tam_1,tam_2,lista_c,lista_a,lista_b))