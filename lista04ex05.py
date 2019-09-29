ch = input("Caractere: ")
for linha in range(11):
    for coluna in range(10):
        if (linha == coluna):
            print(ch,ch,sep = '', end = '')
        elif linha + coluna == 9:
            print(ch,ch,sep = '', end = '')
        else:
            print('  ',sep = '', end = '')
    print()
