p = 1
print('---------- LOJA TABAJARA -----------1')
n = 1
total = 0

while p != 0:
    p = float(input('Produto {}: R$ '.format(n)))
    n += 1
    total += p
print('------------------------------------')
print('Total: R$ {:.2f} '.format(total))
dinheiro = float(input('Dinheiro: R$ '))
print('Troco: R$ {:.2f}'.format(dinheiro - total))
print('------------------------------------')
