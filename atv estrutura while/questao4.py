total_compra = 0

while True:
    preco = float(input("Digite o preço da mercadoria (ou 0 para finalizar): "))
    
    if preco == 0:
        break # Finaliza o loop
    elif preco < 0:
        print("Preço inválido. Por favor, insira um valor positivo.")
    else:
        total_compra += preco #Equivale a total_compra = total_compra + preco

print(f"Total da compra: R$ {total_compra:.2f}")

# Valor pago
while True:
    valor = float(input("Digite o valor em dinheiro que irá usar para pagar: "))
    
    if valor < total_compra:
        print("Valor pago é menor que o total da compra. Por favor, insira um valor suficiente.")
    else:
        break # Finaliza o loop


troco = valor - total_compra
print(f"Troco a ser devolvido: R$ {troco:.2f}")
