"""O usuário escolhe uma forma de pagamento e o programa informa se há desconto ou acréscimo.

"""

while True:
    print("\n===== CALCULADOR DE PREÇO =====")
    print("1 - A vista")
    print("2 - 6X com juros")
    print("3 - 7X com juros")
    print("4 - 8X com juros")
    print("5 - 9X com juros")
    print("6 - Sair")

    preco = float(input("Digite o preço do produto: "))

    opcao = input("Escolha o numero referente a sua forma de pagamento: ")

    match opcao:
        case "1":
            conta = preco * (1 - 5 / 100)
            print(f"Desconto de 5%: R$ {conta:.2f}")

        case "2":
            conta = preco * (1 + 5 / 100)
            print(f"Acréscimo de 5%: R$ {conta:.2f}")

        case "3":
            conta = preco * (1 + 10 / 100)
            print(f"Acréscimo de 10%: R$ {conta:.2f}")

        case "4":
            conta = preco * (1 + 15 / 100)
            print(f"Acréscimo de 15%: R$ {conta:.2f}")

        case "5":
            conta = preco * (1 + 20 / 100)
            print(f"Acréscimo de 20%: R$ {conta:.2f}")

        case "6":
            print("Saindo... Obrigado por utilizar nosso calculador de preço!")
            break

        case _:
            print("Opção inválida!")