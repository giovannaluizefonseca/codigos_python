while True:
    numero = int(input("Digite um valor inteiro qualquer: "))
    
    if numero < 0:
        print("Programa encerrado.")
        break # Finaliza o loop

    if numero > 100: # Vendo se é maior que 100
        print("Limite excedido")
    elif numero > 10: # Vendo se é maior que 10
        print(f"O quadrado de {numero} é {numero ** 2}")
    elif numero > 5: # Vendo se é maior que 5
        print(f"O cubo de {numero} é {numero ** 3}")
    else:
        print("Valor não atende a nenhum critério.")
