p = int(input('Digite quantas pessoas serão registradas: '))
while p <= 0:
    print('Registre ao menos uma pessoa.')
    p = int(input('Digite quantas pessoas serão registradas: '))
soma = 0
x = 0
while x < p:
    idade = int(input('Digite a idade do aluno: '))
    while idade < 0:
        print('Digite um valor maior ou igual a 0.')
        idade = int(input('Digite a idade do aluno: '))    
    soma += idade
    x += 1
media = soma/p
print('Média de idade da turma: ',media)
if media >= 0 and media <= 25:
    print('A turma é jovem.')
elif media >= 26 and media <= 60:
    print('A turma é adulta.')
elif media > 60:
    print('A turma é idosa.')
