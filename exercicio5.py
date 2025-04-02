"""O usuário informa uma cor em português (vermelho, azul, verde, amarelo), e o programa exibe sua tradução para inglês."""

while True:
    print("\n===== TRADUTOR DE CORES =====")
    print("1 - Vermelho")
    print("2 - Azul")
    print("3 - Verde")
    print("4 - Amarelo")
    print("5 - Sair")

    opcao = input("Escolha o numero da sua cor: ")

    match opcao:
        case "1":
            print("RED")

        case "2":
            print("BLUE")

        case "3":
            print("GREEN")

        case "4":
            print("YELLOW")

        case "5":
            print("Saindo... Obrigado por utilizar nosso tradutor de cores!")
            break

        case _:
            print("Opção inválida!")