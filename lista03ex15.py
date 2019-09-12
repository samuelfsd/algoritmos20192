v = int(input('Digite um valor: '))
primo = True
for i in range(2,v,1):
    if v %i ==0:
        primo = False
if primo:
        print('É primo')
else:
    print('Não é primo')
