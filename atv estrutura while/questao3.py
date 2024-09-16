import random

numero = random.randint(1, 100) # Vai gerar um número aleatório entre 1 e 100
tentativas = 5

print("Tente adivinhar o número entre 1 e 100. Você tem 5 tentativas.")

while tentativas > 0:
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero:
        print("O número secreto é maior.")
    elif palpite > numero:
        print("O número secreto é menor.")
    else:
        print("Parabéns! Você acertou o número!")
        break # Finaliza o loop

    tentativas -= 1 # Equivale a tentativas = tentativas - 1

    print(f"Tentativas restantes:{tentativas}")

if tentativas == 0:
    print(f"Você não acertou o número. O número secreto era: {numero}")