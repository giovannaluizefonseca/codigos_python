import random

resultados = []

while True:
    resultado = random.choice(["Cara", "Coroa"])
    resultados.append(resultado)
    print(f"Resultado: {resultado}")

    continuar = input("Deseja lançar a moeda novamente? (sim/nao): ")
    if continuar != 'sim':
        break

print("Resultados dos lançamentos:", resultados)
