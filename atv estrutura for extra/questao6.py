numero = int(input("Digite um número inteiro: "))
soma_divisores = 0

if numero <= 1:
    print(f"{numero} não é um número perfeito.")
else:
    for valor in range(1, numero):
        if numero % valor == 0:  # Saber se valor é um divisor do numero
            soma_divisores += valor # Equivale a soma_divisores = soma_divisores + valor
    
    if soma_divisores == numero:
        print(f"{numero} é um número perfeito.")
    else:
        print(f"{numero} não é um número perfeito.")
