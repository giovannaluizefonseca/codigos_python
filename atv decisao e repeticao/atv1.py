def calcular_calorias(atividade, tempo):
    if atividade == "caminhada":
        calorias = 5 * tempo
    elif atividade == "corrida":
        calorias = 10 * tempo
    elif atividade == "ciclismo":
        calorias = 8 * tempo
    else:
        calorias = 0
    print(f"Você queimou um total de {calorias} calorias com {atividade} por {tempo} minutos.")

while True:
    atividade = input("Informe o tipo de atividade (caminhada, corrida, ciclismo) ou 'sair' para encerrar: ").lower()
    if atividade == 'sair':
        print("Encerrando o programa.")
        break
    
    if atividade == "caminhada":
        tempo = float(input("Informe o tempo em minutos: "))
        if tempo >= 0:
            calcular_calorias(atividade, tempo)
        else:
            print("O tempo não pode ser negativo. Tente novamente.")
    elif atividade == "corrida":
        tempo = float(input("Informe o tempo em minutos: "))
        if tempo >= 0:
            calcular_calorias(atividade, tempo)
        else:
            print("O tempo não pode ser negativo. Tente novamente.")
    elif atividade == "ciclismo":
        tempo = float(input("Informe o tempo em minutos: "))
        if tempo >= 0:
            calcular_calorias(atividade, tempo)
        else:
            print("O tempo não pode ser negativo. Tente novamente.")
