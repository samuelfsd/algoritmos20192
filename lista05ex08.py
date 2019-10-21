n = int(input('Informe o tamanho das listas: '))
a = [0]*n
b = [0]*n
for i in range (n):
    a[i] = int(input('Informe um número: '))
for j in range (n):
    b[j] = int(input('Informe um número: '))
if a == b:
    print ('As listas pssuem os mesmos conteúdos')
