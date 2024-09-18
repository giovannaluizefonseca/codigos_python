valor = int(input("Digite um número de 0 a 100: "))

if 0 <= valor <= 25:
    print("O número está na faixa de 0 a 25.")
elif 26 <= valor <= 50:
    print("O número está na faixa de 26 a 50.")
elif 51 <= valor <= 75:
    print("O número está na faixa de 51 a 75.")
elif 76 <= valor <= 100:
    print("O número está na faixa de 76 a 100.")
else:
    print("Número fora do intervalo permitido.")
