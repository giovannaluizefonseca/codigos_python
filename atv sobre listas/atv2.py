temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
meses_numero = 12
numero_mes = 0

#Organizando os meses em ordem
while True:
    if numero_mes >= meses_numero:
        break

    temp = float(input(f"Insira a temperatura média de {meses[numero_mes]}: "))
    temperaturas.append(temp)
    numero_mes += 1

#Pegando as temperaturas
total_temperaturas = 0
numero = 0

while True:
    if numero >= meses_numero: #Se atingiu o número total de meses (12)
        break
    total_temperaturas += temperaturas[numero] #Adiciona temperatura através de numero para total_temperaturas
    numero += 1

media_anual = total_temperaturas / meses_numero

print(f"A média anual das temperaturas é: {media_anual:.2f}°C")

#Vendo quais estão acima da média
acima_media = 0

while True:
    if numero_mes >= meses_numero:
        break
    else:
        temperaturas[acima_media] > media_anual
        print(f"{meses[numero_mes]}: {temperaturas[numero_mes]:.2f}°C")
        numero_mes += 1