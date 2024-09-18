numeros = []

for contador in range(5):
    valor = int(input("Digite um número inteiro: "))
    numeros.append(valor)


print(f"Lista completa é: {numeros}")


print(f"Valores divisíveis por 3:")
for numero in numeros:
    if numero % 3 == 0:
        print(numero, end=", ")