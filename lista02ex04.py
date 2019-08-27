n1 = int(input ('Informe um número: '))
n2 = int(input ('Informe outro número: '))
n3 = int(input ('Informe outro número: '))
if n1 > n2 > n3:
    print ('O maior valor foi', n1 ,'e','o menor valor foi', n3,'.')
elif n2 > n1 > n3:
    print ('O maior valor foi', n2 ,'e','o menor valor foi', n3,'.')
elif n3> n2 >n1:
    print ('O maior valor foi', n3 ,'e','o menor valor foi', n1,'.')
elif n2 > n3 > n1:
    print ('O maior valor foi', n2 ,'e','o menor valor foi', n1,'.')
elif n1> n3 > n2 : 
    print('O maior valor foi', n1 ,'e','o menor valor foi', n2,'.')
else:
    print ('O maior valor foi', n3 ,'e','o menor valor foi', n2,'.')
    
