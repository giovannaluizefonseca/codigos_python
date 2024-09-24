notas = []

nota = -1  # Inicializa com um valor diferente de zero
while nota == 0:
    nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
    if nota == 0:
        notas.append(nota)

soma = 0
quantidade = 0

for nota in notas:
    soma += nota
    quantidade += 1

media = soma / quantidade if quantidade > 0 else 0

acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1

print(f"Quantidade de alunos com nota acima da média: {acima_media}")