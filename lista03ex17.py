turma = int(input('Quantas turmas serão registradas: '))
while turma < 1:
    print('Registre ao menos uma turma.')
    turma = int(input('Quantas turmas serão registradas: '))
x = 0
soma = 0
while x < turma:
    t = int(input('Digite quantos alunos tem na turma: '))
    while t < 0 or t > 40:
        if t < 0:
            print('Digite um valor maior ou igual a 0.')
        elif t > 40:
            print('Uma turma não pode ter mais do que 40 alunos.')
        print('Digite novamente.')
        t = int(input('Digite quantos alunos tem na turma: '))
    soma += t
    x += 1
print('Número de turmas:',turma)
print('Total de alunos:',soma)
print('Média de alunos: ',(soma/turma))
