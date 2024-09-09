nome = input("Informe o seu nome: ")
sexo = input("Informe se é do sexo F ou M : ")
estcivil = input("Informe se é casada(o) ou solteira(o): ")


if sexo == "F" and estcivil == "casada":
    anos_casada = float(input("Informe o seu tempo de casada em anos: "))
    print(f"O seu nome é {nome} e seu tempo de casada é {anos_casada} anos")
else:
    print(f"O seu nome é {nome}, obrigada e até a próxima")
