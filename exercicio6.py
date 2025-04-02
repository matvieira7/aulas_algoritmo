"""O usuário seleciona uma opção de atendimento telefônico:

1 - Suporte Técnico

2 - Financeiro

3 - Cancelamento

4 - Falar com um atendente"""

while True:
    print("\n===== CENTRAL DE ATENDIMENTO =====")
    print("1 - Suporte Técnico")
    print("2 - Financeiro")
    print("3 - Cancelamento")
    print("4 - Falar com atendente")
    print("5 - Sair")

    opcao = input("Escolha o numero referente ao seu atendimento desejado: ")

    match opcao:
        case "1":
            print("Aguarde enquanto transferimos o técnico para o chat")

        case "2":
            print("Aguarde enquanto transferimos o agente do financeiro para o chat ")

        case "3":
            print("Aguarde enquanto preparamos o seu cancelamento")

        case "4":
            print("Aguarde enquanto transferimos o atendente para o chat")

        case "5":
            print("Saindo... Obrigado por utilizar nossa central de atendimento!")
            break

        case _:
            print("Opção inválida!")