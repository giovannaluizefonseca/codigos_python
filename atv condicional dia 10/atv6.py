valor_compra = float(input("Digite o valor da compra: R$"))
parcelas = int(input("Digite o número de parcelas desejadas (de 1 a 24): "))

# Calculando o valor da parcela e o total que vai ser pago
if parcelas < 1 or parcelas > 24:
    resultado = "Número de parcelas inválido. Deve ser de 1 a 24."
else:
    juros = 0.015  # 1.5% de juros
    valor_acrescentado = 6  # Valor que vai ser acrescentado para parcelas acima de 12

    if parcelas > 12:
        valor_total = valor_compra * (1 + juros)
        valor_parcela = valor_total / parcelas + valor_acrescentado
    else:
        valor_total = valor_compra
        valor_parcela = valor_total / parcelas

    resultado = f"Valor total a ser pago: R${valor_total:.2f}\nValor de cada parcela: R${valor_parcela:.2f}"

# Mostra o resultado
print(resultado)