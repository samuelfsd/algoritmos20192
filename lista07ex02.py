def prova_candidato(tam):
    lista_candidato = ['']*tam
    for i in range (tam):
        lista_candidato[i] = str(input(f'Informe as suas respostas: Questão {i+1} \n'))
    return lista_candidato
def prova_gabarito (tam):
    lista_gabarito = ['']*tam
    for i in range (tam):
        lista_gabarito[i] = str(input(f'Informe a resposta do gabarito: Questão {i+1} \n '))
    return lista_gabarito
def prova_acertos (tam,candidato,gabarito):
    nota = 0
    for i in range (tam):
        if candidato[i] == gabarito[i]:
            nota += 1 
    nota = (nota/tam)*100 
    return nota
tam = int(input('Informe quantas questões são:\n'))
candidato = prova_candidato(tam)
gabarito = prova_gabarito(tam)
acertos = prova_acertos(tam,candidato,gabarito)
print ('A sua porcentagem de acerto é de {:.2f}%'.format(acertos))