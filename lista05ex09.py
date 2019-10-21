x = int(input('Quantos números a lista deve ter: '))
valor = 0
cont = ['']
a = [0]*x
par = []
imp = []
for i in range (x):
    valor = int(input('Informe os números: '))
    a[i] = valor
    cont[0] = valor
    if valor % 2 == 0:
        par = par + cont   
    else:
        imp = imp + cont     
print ('Vetor informado pelo usuário: ',a)
print ('Os valores pares desse vetor: ',par)
print ('Os valores ímpares desse vetor: ',imp)
