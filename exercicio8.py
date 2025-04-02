"""O usuário escolhe um destino (São Paulo, Rio de Janeiro, Curitiba, Salvador) e recebe o valor da passagem."""

while True:
    print("\n===== VITRINE DE PASSAGENS =====")
    print("1 - São Paulo")
    print("2 - Rio de Janeiro")
    print("3 - Curitiba")
    print("4 - Salvador")
    print("5 - Sair")

    opcao = input("Escolha o numero referente ao seu destino de viagem: ")

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
            print("Saindo... Obrigado por utilizar nossa vitrine de passagens!")
            break

        case _:
            print("Opção inválida!")