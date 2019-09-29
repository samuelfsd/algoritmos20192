ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 1 == 0:
            print(ch,ch,sep = '', end = '')
        else:
            print(' ',  end = '')
    print()
