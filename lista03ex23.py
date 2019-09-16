print('Tabela de parcelas com juros:')
print('Quantidade de parcelas:  %juros sobre o valor inicial da compra:')
print('         - 1 -                                    - 0 -')
print('         - 3 -                                    - 10 -')
print('         - 6 -                                    - 15 -')
print('         - 9 -                                    - 20 -')
print('         - 12-                                    - 25 -')
divida = float(input('Informe o valor da dívida: '))
dez1 = 0.10 * divida
dez2 = (0.10 * divida) + divida
dez3 = dez2 / 3
quinze1 = 0.15 * divida
quinze2 = (0.15 * divida) + divida
quinze3 = quinze2 / 6
vinte1 = 0.20 * divida
vinte2 = (0.20 * divida) + divida
vinte3 = vinte2 / 9
vintecinco1 = 0.25 * divida
vintecinco2 = (0.25 * divida) + divida
vintecinco3 = vintecinco2 / 12
print ('Valor da Divida -- Valor dos Juros -- Quantidade de Parcelas -- Valor da parcela  ')
print ('R$:',divida,'             0                      1                  R$:',divida,   )
print ('R$:',dez2,'            ',dez1,'                  3                 R$:{:.2f}'.format(dez3),     )
print ('R$:',quinze2,'            ',quinze1,'                  6                  R$:{:.2f}'.format(quinze3),     )
print ('R$:',vinte2,'            ',vinte1,'                  9                  R$:{:.2f}'.format(vinte3),     )
print ('R$:',vintecinco2,'            ',vintecinco1,'                  12                  R$:{:.2f}'.format(vintecinco3),     )


       
