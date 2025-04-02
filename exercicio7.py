"""O usuário escolhe uma operação matemática (+, -, *, /) e insere dois números. O programa exibe o resultado."""

while True:
    print("\n===== MINI CALCULADORA =====")
    print("1 - Soma(+)")
    print("2 - Subtração(-)")
    print("3 - Multiplicação(*)")
    print("4 - Divisão(/)")
    print("5 - Sair")

    num1 = float(input("Digite o 1 numero: "))

    opcao = input("Escolha o numero referente a sua operação desejada: ")

    num2 = float(input("Digite o 2 numero: "))

    match opcao:
        case "1":
            conta = num1 + num2
            print(f"{conta:.2f}")

        case "2":
            conta = num1 - num2
            print(f"{conta:.2f}")

        case "3":
            conta = num1 * num2
            print(f"{conta:.2f}")

        case "4":
            conta = num1 / num2
            print(f"{conta:.2f}")

        case "5":
            print("Saindo... Obrigado por utilizar nossa mini calculadora!")
            break

        case _:
            print("Opção inválida!")