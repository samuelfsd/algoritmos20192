gabarito = ['']*10
aluno = [0]*10
acertos = 0
print ('Informe o gabarito: Letras de A até E ')
for i in range (10):
    gabarito[i] = input('Questão {}:'.format(i + 1))
    while gabarito[i] > 'E':
        gabarito[i] = input('Resposta inválida, informe as letras de A até E.')
print ('Gabarito finalizado. ')
alunos = int(input('Número de alunos: '))
for i in range (alunos):
    print ('Aluno {}: '.format(i+1))
    for j in range (10):
        aluno[j] = input('Questão {}: '.format(j+1))
        if aluno[j] == gabarito[j]:
            acertos +=  1 
    print ('Respostas do aluno {}: '.format(i+1))
    for k in range (10):
        print ('Questão {}: {}'.format(k+1,aluno[k]))
    print ('Número de acertos: {}'.format(acertos))
    acertos = 0
        
                        
    
