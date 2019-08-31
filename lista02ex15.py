print ('Gasolina R$ 4,50 litro. Álcool R$ 3,40.' )
combus = input('Digite (G) para gasolina e (A) para Álcool: ')
litros = float(input('Informe a quantidade de litros que você deseja: '))
a = 3.40 * litros
g = 4.50 * litros
if combus == 'A' and litros < 20:
    a1 = a - (3/100 * a)
    print ('Total R$', a1)
elif combus == 'A' and litros >= 20:
    a2 = a - (5/100 * a)
    print ('Total R$', a2)
if combus == 'G' and litros < 20:
    g1 = g - (4/100 * g)
    print ('Total R$', g1)
elif combus == 'G' and litros >= 20:
    g2 = g - (4/100 * g)
    print ('Total R$', g2)
