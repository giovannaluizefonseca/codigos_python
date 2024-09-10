numero_ano = int(input("Informe um ano: "))

if (numero_ano % 400 == 0) or (numero_ano % 4 == 0 and numero_ano % 100 != 0): # !=0, quer dizer que não é divisível
    print(f"O ano {numero_ano} é bissexto.")
else:
    print(f"O ano {numero_ano} não é bissexto.") 