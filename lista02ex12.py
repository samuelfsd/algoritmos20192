num = int(input('Digite um número inteiro menor que 1000: '))
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print (num, '=', c, 'centena(s),', d, 'dezena(s) e', u, 'unidade(s).')
