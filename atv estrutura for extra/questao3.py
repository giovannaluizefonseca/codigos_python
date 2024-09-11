media = 33.5
acima_igual = 0
abaixo = 0

for n in range(7):
    temperatura = float(input(f"Digite a temperatura {n + 1}: "))
    
    if temperatura >= media:
        acima_igual += 1
    elif temperatura < media:
        abaixo += 1

print(f"Quantas temperaturas são iguais ou estão acima da média: {acima_igual}")
print(f"Quantas temperaturas estão abaixo da média: {abaixo}")