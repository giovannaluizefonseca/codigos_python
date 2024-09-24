def gerenciar_eventos():
    eventos = []
    
    while True:
        menu = input("Digite 'adicionar' para adicionar um evento, 'remover' para remover, ou 'sair' para encerrar: ")
        
        if menu == 'adicionar':
            evento = input("Digite o evento para adicionar: ")
            eventos.append(evento)
        elif menu == 'remover':
            evento = input("Digite o evento para remover: ")
            if evento in eventos:
                eventos.remove(evento)
            else:
                print("Evento não encontrado.")
        elif menu == 'sair':
            break
        else:
            print("Ação inválida.")

        print(f"Eventos atuais: {eventos}")

gerenciar_eventos()

