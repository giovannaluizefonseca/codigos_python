valorA = int(input("Informe um valor numérico A: "))
valorB = int(input("Informe um valor numérico B: "))

if valorA==valorB:
    valorC = valorA+valorB 
    input(f"A soma dos valores é: {valorC}")
else:
    valorC = valorA*valorB
    input(f"A multiplicação dos valores é: {valorC}")