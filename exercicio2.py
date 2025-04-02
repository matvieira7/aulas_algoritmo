"""2 . Cálculo de Área de Figuras Geométricas

Desenvolva um programa que permita ao usuário escolher entre calcular a área de um quadrado, retângulo ou triângulo e insira os valores necessários para o cálculo."""

while True:
    print("\n===== CALCULADOR DE ÁREAS =====")
    print("1 - Triângulo")
    print("2 - Retângulo")
    print("3 - Quadrado")
    print("4 - Sair")

    opcao = input("Escolha o numero da sua área: ")

    match opcao:
        case "1":
            base = float(input("Digite o valor da base do triângulo: "))
            altura = float(input("Digite o valor da altura do triângulo: "))
            area = (base * altura)/2
            print(f"A área do seu triângulo é de: {area:.2f}")

        case "2":
            base = float(input("Digite o valor da base do retângulo: "))
            altura = float(input("Digite o valor da altura do retângulo: "))
            area = base * altura
            print(f"A área do seu retângulo é de: {area:.2f}")

        case "3":
            lado = float(input("Digite o valor do lado do quadrado: "))
            area = lado * lado
            print(f"A área do seu quadrado é de: {area:.2f}")

        case "4":
            print("Saindo... Obrigado por utilizar nosso calculador de áreas!")
            break

        case _:
            print("Opção inválida!")