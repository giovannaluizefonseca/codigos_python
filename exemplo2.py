nome = "Luize Giovanna"
end = "Av Castelo Branco"
idade = "18"

# print(nome, end, idade)
# 1º forma de concatenação
print("Olá ",nome," seu endereço ",end," sua idade é ",idade)

# 2º forma de concatenação
print("Seja bem vindo {} sua residência está na {} e você possui {} anos".format(nome,end,idade))

# 3º forma de concatenação - f string
print(f"Olá, seja bem vindo {nome}, o seu endereço é {end} e sua idade é {idade}")