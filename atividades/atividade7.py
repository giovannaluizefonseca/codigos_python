preco = int(input("Informe o preço: "))
pagamento = int(input("Informe a condição de pagamento: 1-Pix, dinheiro ou débito, 2-À vista no cartão de crédito, 3-Em duas vezes, preço normal sem juros, 4-Em três vezes, preço normal mais juros de 10%: "))

if pagamento == 1:
    desconto = preco*0,15
    precofinal = preco - desconto
    print(f"O preço final a ser pado é de {precofinal:.2f} reais")
elif pagamento == 2:
    desconto = preco*0.10
    precofinal = preco - desconto
    print(f"O preço final a ser pago é de {precofinal:.2f} reais")
elif pagamento == 3:
    print(f"O preço final a ser pago é de {preco:.2f} reais")
elif pagamento == 4:
    desconto = preco*0,10
    precofinal = preco + desconto
    print(f"O preço final a ser pago é de {precofinal:.2f} reais")
else:
    print(f"A condição de pagamento não foi escolhida")