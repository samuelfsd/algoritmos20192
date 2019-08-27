nota = float(input ('Informe sua primeira nota: '))
nota2 = float(input ('Informe sua segunda nota: '))
nota3 = (nota + nota2) / 2
if nota3 >= 7:
    print ('Parabéns aprovado!')
elif nota3 >= 5 <7:
    print ('Ih rapaz, vai ter que estudar para prova final.')
else:
    print ('Não estudou o suficiente, está reprovado.')
    
