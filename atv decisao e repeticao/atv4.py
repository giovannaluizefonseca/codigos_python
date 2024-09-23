import random

def jogar():
    while True:
        print("Escolha:")
        print("1: Pedra")
        print("2: Papel")
        print("3: Tesoura")

        usuario = int(input("Sua escolha (1, 2 ou 3): "))
        
        computador = random.randint(1, 3) #Escolhe um número aleatório de 1 a 3
        escolhas = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

        print(f"Computador escolheu: {escolhas[computador]}")

        if usuario == computador:
            resultado = "Empate!"
        elif usuario == 1:
            if computador == 3:
                resultado = "Você ganhou!"
            else:
                resultado = "Você perdeu!"
        elif usuario == 2:
            if computador == 1:
                resultado = "Você ganhou!"
            else:
                resultado = "Você perdeu!"
        elif usuario == 3:
            if computador == 2:
                resultado = "Você ganhou!"
            else:
                resultado = "Você perdeu!"

        print(resultado)

        continuar = input("Deseja jogar novamente? (sim/nao): ")
        if continuar == 'sim':
            print("Encerrando o jogo.")
            break

jogar()
