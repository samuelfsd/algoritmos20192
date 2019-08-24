salario = float (input ('Qual o seu salário atual? '))
percentual = float (input ('Qual o percentual do reajuste? '))
reajuste = salario * (percentual / 100) + salario
print ('O salário com o reajuste vai ficar', reajuste ,' reais.')
