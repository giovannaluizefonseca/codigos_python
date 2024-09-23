import time

segundos = int(input("Digite o número de segundos para a contagem regressiva: "))

for tempo in range(segundos, 0, -1): #-1 indica que estamos contando para baixo.
    print(f"Tempo restante: {tempo} segundos")
    time.sleep(1)  #Pausa de 1 segundo

print("Tempo esgotado!")
