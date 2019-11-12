print ('Informe as respostas de cada aluno, podendo ser A,B,C ou D: ')
respostas = []
for i in range(5):
    respostas.append([0]*10)
for i in range(5):
    for j in range(10):
        respostas[i][j] = input('Aluno {}, Questão {}: '.format(i+1,j+1)).upper()
        while respostas[i][j]!='A' and respostas[i][j]!='B' and respostas[i][j]!='C' and respostas[i][j]!='D' and respostas[i][j] != 'a' and respostas[i][j]!= 'b' and respostas[i][j] != 'c' and respostas[i][j] != 'd':
            respostas[i][j] = input('Resposta inválida, deve ser A,B,C ou D, tente novamente: ')
gabarito = [0] * 10
for i in range(10):
    gabarito[i] = input('Gabarito para questão {}: '.format(i+1)).upper()
    while gabarito[i]!='A' and gabarito[i]!='B' and gabarito[i]!='C' and gabarito[i]!='D'and gabarito[i] !='a' and gabarito[i] != 'b' and gabarito[i] != 'c' and gabarito[i] != 'd':
        gabarito[i] = input('Resposta inválida, deve ser A,B,C ou D, tente novamente: ') #a vida seria melhor sem questões de gabarito de alunos
resultado = [0]*5
def corrige():
    nota = 0
    for i in range(5):
        nota = 0
        for j in range(10):
            if respostas[i][j] == gabarito[j]:
                nota = nota + 1
        resultado[i] = nota
    return nota
resultado.append(corrige())
for i in range(5):
    print('Nota do aluno {}: {}'.format(i+1,resultado[i]))
