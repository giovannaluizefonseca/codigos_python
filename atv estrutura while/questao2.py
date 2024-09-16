import datetime # O módulo é importado para que o programa possa obter a data e hora atuais

ano_atualmente = datetime.datetime.now().year # Consegue a data e hora de agora, e .year extrai apenas o ano da data
ano_nascimento = 0

while True:
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    
    idade = ano_atualmente - ano_nascimento
    
    if idade >= 18:
        print("Inscrição realizada com sucesso!")
        break # Finalizar o loop
    else:
        print("Você deve ter 18 anos ou mais para se inscrever. Tente novamente.")