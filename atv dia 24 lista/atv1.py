# Lê os números da primeira lista
entrada1 = input("Digite os números da primeira lista (separados por espaço): ")
lista1 = []
numero = ""
i = 0

while True:
    caractere = entrada1[i:i+1]  # Pega um caractere
    if caractere == '':  # Verifica se chegou ao fim
        break
    if caractere == ' ':
        if numero:
            lista1.append(int(numero))
            numero = ""
    else:
        numero += caractere
    i += 1

if numero:
    lista1.append(int(numero))

# Lê os números da segunda lista
entrada2 = input("Digite os números da segunda lista (separados por espaço): ")
lista2 = []
numero = ""
i = 0

while True:
    caractere = entrada2[i:i+1]  # Pega um caractere
    if caractere == '':  # Verifica se chegou ao fim
        break
    if caractere == ' ':
        if numero:
            lista2.append(int(numero))
            numero = ""
    else:
        numero += caractere
    i += 1

if numero:
    lista2.append(int(numero))

intersecao = []

# Encontra a interseção
for num in lista1:
    if num in lista2 and num not in intersecao:
        intersecao.append(num)

# Ordena a interseção manualmente
for i in range(100):  # Limita a 100 eventos, ajuste conforme necessário
    if i < 100:  # Para não ultrapassar o limite
        for j in range(i + 1, 100):
            if j < 100 and intersecao[i:i+1] != '':
                if intersecao[i] > intersecao[j]:
                    intersecao[i], intersecao[j] = intersecao[j], intersecao[i]

# Exibe os números em comum
print("Números em comum (ordem crescente):", intersecao)