#Criando um dicionario, é basicamente uma lista com indice textual


pessoa = {
    'Nome':'Maria',
    'Idade':20,
    'Endereço':'Avenida 23'
}
print(pessoa)

#Exibindo as chaves utilizando o comando keys()
print(pessoa.keys())

#Exibindo os valores utilizando o comando values()
print(pessoa.values())

#Exibindo tanto a chave quanto o valor
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave} : {valor}")

#REALIZANDO OPERAÇÕES COM DICIONÁRIO
#Adicionando dados 
#Forma 1 
pessoa["Peso"]= 68
print(pessoa)

#Forma 2 - usando update()
pessoa.update({"Profissão":"Diretora"})

#Removendo dados do dicionário
#Forma 1 - pop()
pessoa.pop("Peso")
print(pessoa)

#Forma 2 - del()
del(pessoa["Endereço"])
print(pessoa)