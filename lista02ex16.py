print ('Tabela de Preços:')
print ('Morango até 5 KG R$ 2,50 o KG. Acima de 5 KG R$ 2,20 o KG.')
print ('Maçã até 5 KG R$ 1,80 o KG. Acima de 5 KG R$ 1,50 o KG.')
print ('OBS: caso a compra ultrapasse 8 KG de frutas ou R$ 25,00 serão incluidos 10% de desconto.')
mo = 2.50
ma = 1.80
morango = float(input('Informe quantos KG de morango você quer: '))
if morango <= 5:
    mo = mo * morango
else:
    mo = (mo - 0.30) * morango  
maca = float(input('Informe quantos KG de maças você quer: '))
if maca <= 5:
    ma = ma * maca
else:
    ma = (ma - 0.30) * maca 
total = mo
print ('Morangos: R$', mo)
total2 = ma
print ('Maça: R$', ma)
total3 = total + total2
print ('Total R$', total3)
if morango + maca > 8:
    print ('Total com desconto R$', total3 - (10/100) * total3)
