valor_inicial = int(input("Insira um valor inicial: "))
valor_final = int(input("Insira um valor final: "))
soma = 0 #Calcula a soma dos números inteiros no intervalo

for contador in range(valor_inicial, valor_final + 1):
    soma += contador

#Mostrar resultado

print(f"O resultado da soma dos números inteiros entre {valor_inicial} e {valor_final} é: {soma}")