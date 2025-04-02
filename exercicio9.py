"""O usuário escolhe um produto e o programa informa o preço.

"""

while True:
    print("\n===== LOJA VIRTUAL =====")
    print("1 - Jogo de Panelas")
    print("2 - Edição Deluxe EAFC25")
    print("3 - Boneco do Max Steel")
    print("4 - Fone Pulse Elite")
    print("5 - PS5 Slim")
    print("6 - Sair")

    opcao = input("Escolha o numero referente ao seu produto desejado: ")

    match opcao:
        case "1":
            print("R$194,00")

        case "2":
            print("R$541,00")

        case "3":
            print("R$174,14")

        case "4":
            print("R$976,00")

        case "5":
            print("R$3500,00")

        case "6":
            print("Saindo... Obrigado por utilizar nossa loja virtual!")
            break

        case _:
            print("Opção inválida!")