numero1 = 0
numero2 = 0
numero3 = 0
numero4 = 0
numero5 = 0
numero6 = 0
numero7 = 0
numero8 = 0

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))
numero6 = int(input("Digite o sexto número: "))
numero7 = int(input("Digite o sétimo número: "))
numero8 = int(input("Digite o oitavo número: "))

numeros_negativos = 0
soma_positivos = 0
numeros = (numero1, numero2, numero3, numero4, numero5, numero6, numero7, numero8)

for numero in numeros:
    if numero < 0:
        numeros_negativos += 1  # Equivale a numeros_negativos = numeros_negativos + 1, contando os valores negativos
    elif numero > 0:
        soma_positivos += numero  # Soma os números positivos

print(f"Quantidade de números negativos:{numeros_negativos}")
print(f"Soma dos números positivos:{soma_positivos}")
