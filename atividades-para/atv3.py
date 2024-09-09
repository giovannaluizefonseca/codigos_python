numero = int(input("Insira um número inteiro: "))

for contador in range(1, numero + 1):
    if numero % contador == 0:
        print(contador)

print(f"Os divisores do {numero} são:")