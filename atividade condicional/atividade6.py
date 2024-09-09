valorA = float(input("Informe um valor numérico A: "))
valorB = float(input("Informe um valor numérico B: "))
valorC = float(input("Informe um valor numérico C: "))

#Ordenando
def ordem_valores(valorA, valorB, valorC):
    if valorA > valorB:
        valorA, valorB
    if valorA > valorC:
        valorA, valorC
    if valorB > valorC:
        valorB, valorC
    print(f"Os valores em ordem ascendente é {valorA}, {valorB}, {valorB}")

ordem_valores(valorA, valorB, valorC)