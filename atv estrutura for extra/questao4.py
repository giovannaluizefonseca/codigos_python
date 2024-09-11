maior_numero = 0

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))

    if maior_numero == 0: # Se 'maior_numero' ainda é 0, então é o primeiro número inserido
        maior_numero = numero
    elif numero > maior_numero: # Se o número atual é maior que o maior número registrado, atualiza 'maior_numero'
        maior_numero = numero

print(f"O maior número informado é: {maior_numero}")
