"""O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis), e o programa exibirá o percentual de desconto correspondente."""

while True:
    print("\n===== MOSTRAR DESCONTO =====")
    print("1 - Eletrônico")
    print("2 - Roupas")
    print("3 - Alimentos")
    print("4 - Móveis")
    print("5 - Sair")

    opcao = input("Escolha o numero do seu produto desejado: ")

    match opcao:
        case "1":
            print("5% de desconto")

        case "2":
            print("10% de desconto")

        case "3":
            print("15% de desconto")

        case "4":
            print("20%% de desconto")

        case "5":
            print("Saindo... Obrigado por utilizar nosso programa de descontos!")
            break

        case _:
            print("Opção inválida!")