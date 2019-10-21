a = [0]*20
b = [0]*20
c = [0]*20
d = [0]*20
e = [0]*20
for i in range (20):
    a[i] = int(input('Informe um número: Para o 1 Vetor: '))
    b[i] = int(input('Informe um número: Para o 2 Vetor: '))
    c[i] = a[i] - b[i]
    d[i] = a[i] + b[i]
    e[i] = a[i] * b[i]
print ('Primeiro vetor: ',a)
print ('Segundo vetor: ',b)
print ('A diferença entre o vetor 1 e 2: ',c)
print ('A soma entre o vetor 1 e 2: ',d)
print ('O produto entre o vetor 1 e 2: ',e)

