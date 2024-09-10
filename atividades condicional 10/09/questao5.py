
qtd_horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))

if qtd_horas > 40:

    # Calculando as horas extras
    horas_extras = qtd_horas - 40
    valor_regular = 40 * valor_hora
    valor_extra = horas_extras * valor_hora * 0.5
    salario_total = valor_regular + valor_extra
elif qtd_horas >= 0:

    # Calculando o salário normal
    salario_total = qtd_horas * valor_hora
else:

    # Se o usuário colocar um número negativo de horas
    salario_total = 0
    print("Erro: A quantidade de horas trabalhadas não pode ser negativa.")

# Mostrando o resultado
print(f"O salário total do funcionário é: R${salario_total:.2f}")