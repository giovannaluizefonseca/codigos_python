nota_final = float(input("Digite a nota final do aluno: "))
frequencia = float(input("Digite a frequência do aluno em porcentagem: "))

if nota_final >= 7 and frequencia >= 75:
    resultado = "Aprovado"
elif nota_final < 7:
    resultado = "Reprovado"
elif frequencia < 75:
    resultado = "Reprovado"
else:
    resultado = "Não definido"  # Se não encaixar nos critérios citados

# Mostra o resultado
print(f"O aluno está: {resultado}")