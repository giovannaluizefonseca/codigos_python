a = int(input("Digite o primeiro número inteiro positivo A: "))
b = int(input("Digite o segundo número inteiro positivo B: "))
contador = 0

if a <= 0 or b <= 0:
    print("Os números devem ser inteiros positivos.") # Saber se os números são positivos
elif a > b:
    print("O primeiro número deve ser menor ou igual ao segundo número.") # O valor A deve ser menor que o valor B
else:
    for numero in range(a, b + 1):
        if numero % 7 == 0 and numero % 11 == 0:  # Saber se o número é múltiplo de 7 e 11
            contador += 1
       
print(f"Total de números entre {a} e {b} que são múltiplos de 7 e 11 simultaneamente: {contador}")
