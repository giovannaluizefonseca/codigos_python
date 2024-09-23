while True:
    valor_conta = float(input("Informe o valor da conta em R$: "))
    percentual_gorjeta = float(input("Informe o percentual de gorjeta (exemplo: 10 para 10%): "))
    
    gorjeta = valor_conta * (percentual_gorjeta / 100)
    total = valor_conta + gorjeta
    
    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total: R$ {total:.2f}")
