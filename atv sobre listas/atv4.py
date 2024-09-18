numeros = []

for ordem in range(10):
    valor = int(input(f"Insira o {ordem + 1}º número inteiro: "))
    numeros.append(valor)

print(f"Lista preenchida: {numeros}")

posicoes = []
elemento = 0

while elemento < 10:  # A lista terá 10 elementos
    if numeros[elemento] == 3:
        posicoes.append(elemento)
    elemento += 1 #Equivale a elemento = elemento + 1

if posicoes:
    print(f"O número 3 aparece nas posições: {posicoes}")
else:
    print("O número 3 não foi encontrado na lista.")
