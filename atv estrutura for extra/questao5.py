import random # Tornando as funções do módulo random disponíveis no seu código.

contagem = [0, 0, 0, 0, 0, 0] # Contagem dos valores

for n in range(10):
    resultado = random.randint(1, 6)  # Vai gerar um número inteiro aleatório entre 1 e 6.
    
    if resultado == 1:
        contagem[0] += 1 # Equivale a contagem(0) = 0 + 1
    elif resultado == 2:
        contagem[1] += 1 # Equivale a contagem(0) = 1 + 1
    elif resultado == 3:
        contagem[2] += 1 # Equivale a contagem(0) = 2 + 1
    elif resultado == 4:
        contagem[3] += 1 # Equivale a contagem(0) = 3 + 1
    elif resultado == 5:
        contagem[4] += 1 # Equivale a contagem(0) = 4 + 1
    elif resultado == 6:
        contagem[5] += 1 # Equivale a contagem(0) = 5 + 1

print("Resultados dos lançamentos de dados:")
for numero in range(6):
    print(f"Valor {numero + 1}: {contagem[numero]} vezes") # Contagem[numero] conta quantas vezes cada valor do dado (de 1 a 6) aparece nos lançamentos simulados.