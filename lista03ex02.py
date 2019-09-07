usuario = input('Informe o seu usuário: ')
senha = input ('Informe sua senha: ')
while senha == usuario:
    print ('Erro. A senha não pode ser a mesma que o usuário.')
    usuario = input('Informe o seu usuário: ')
    senha = input ('Informe sua senha: ')
print ('Login feito.')
