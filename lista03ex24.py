print ('Para o uso exclusivo do professor: ')
p1 = str(input('Resposta da questão 01: '))
p2 = str(input('Resposta da questão 02: '))
p3 = str(input('Resposta da questão 03: '))
p4 = str(input('Resposta da questão 04: '))
p5 = str(input('Resposta da questão 05: '))
p6 = str(input('Resposta da questão 06: '))
p7 = str(input('Resposta da questão 07: '))
p8 = str(input('Resposta da questão 08: '))
p9 = str(input('Resposta da questão 09: '))
p10 = str(input('Resposta da questão 10: '))
usuario = str(input('O aluno deseja uzar o programa? Digite (S) para Sim ou (N) para Não.'))
contagem = 0
cont = 0
while usuario == 'S':
    aluno = str(input('Informe o seu nome: '))
    contagem = contagem + 1
    print ('Para o uso do discente:')
    a1 = str(input('Resposta da questão 01: '))
    a2 = str(input('Resposta da questão 02: '))
    a3 = str(input('Resposta da questão 03: '))
    a4 = str(input('Resposta da questão 04: '))
    a5 = str(input('Resposta da questão 05: '))
    a6 = str(input('Resposta da questão 06: '))
    a7 = str(input('Resposta da questão 07: '))
    a8 = str(input('Resposta da questão 08: '))
    a9 = str(input('Resposta da questão 09: '))
    a10 = str(input('Resposta da questão 10: '))
    if p1 == a1:
        cont += 1
    if p2 == a2:
        cont += 1
    if p3 == a3:
        cont += 1
    if p4 == a4:
        cont += 1
    if p5 == a5:
        cont += 1
    if p6 == a6:
        cont += 1
    if p7 == a7:
        cont += 1
    if p8 == a8:
        cont += 1
    if p9 == a9:
        cont += 1
    if p10 == a10:
        cont += 1
    print ('Aluno: ',aluno)
    print ('Total de acertos: ',cont)
    print ('Nota: ',cont)
    usuario = str(input('Outro aluno deseja usar o programa? Digite (S) para sim ou (N) para não.'))
media = cont / contagem
print ('Números de alunos: ',contagem)
print ('A média dos alunos é: ',media)

    
            
