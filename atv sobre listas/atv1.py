valores = []
valores_impares = []

while True:
    numero = input("Digite um valor (ou um valor negativo para encerrar): ")
    valor = float(numero)
    
    if valor < 0:
        break #Se for negativo o loop encerra
    else:
        valores.append(valor) #Irá inserir um novo item no final da lista

print(f"Lista de número inseridos: {valores}")

for valor in valores:
    if valor % 2 != 0: #Se o resto da divisão for 0, o número é par
        valores_impares.append(valor) #Adiciona valor caso o número for ímpar

print(f"Lista depois de remover números pares: {valores_impares}")

