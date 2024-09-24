import random

def embaralhar(lista):
    random.shuffle(lista) #Embaralhando a lista usando random.shuffle
    return lista

def jogar():
    # Lista de palavras
    palavras = [
        'Brasil', 'Canadá', 'Japão', 'Austrália', 'França', 'Índia', 'México', 'Itália', 'Egito', 'Argentina', 'Alemanha', 'China', 'Itália', 'Reino Unido', 'Noruega'
    ]
    
    print("A lista de palavras contém os seguintes países:")
    print(palavras)
    
    #Embaralhando a lista
    palavras_embaralhadas = embaralhar(palavras)
    
    #Escolhendo uma palavra aleatória
    palavra_escolhida = random.choice(palavras_embaralhadas)
    posicao_correta = palavras_embaralhadas.index(palavra_escolhida)
    
    print("Adivinhe a posição da palavra escolhida (posição de 0 a 14):")
    
    tentativas = 3
    
    while tentativas > 0:
        tentativa = int(input("Digite sua tentativa: "))
        
        if tentativa == posicao_correta:
            print("Parabéns! Você acertou!")
            break
        else:
            tentativas -= 1
            print(f"Você errou! Tentativas restantes: {tentativas}")
    
    if tentativas == 0:
        print(f"Você esgotou suas tentativas. A palavra estava na posição {posicao_correta}.")
    
    print(f"Lista embaralhada é:{palavras_embaralhadas}")

jogar()

