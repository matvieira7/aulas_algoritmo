"""3. Sistema de Login Simples

O programa deve pedir ao usuário que informe seu nome de usuário e, com base nisso, conceder um nível de acesso:

Admin → Acesso total

Professor → Acesso ao ambiente acadêmico

Aluno → Acesso ao ambiente de estudos"""

while True:
    print("\n===== CONTROLADOR DE ACESSO =====")
    print("1 - Admin")
    print("2 - Professor")
    print("3 - Aluno")
    print("4 - Sair")

    opcao = input("Escolha o numero do seu nivel de acesso: ")

    match opcao:
        case "1":
            print("ACESSO TOTAL!")

        case "2":
            print("Acesso ao ambiente acadêmico")

        case "3":
            print("Acesso ao ambiente de estudos")

        case "4":
            print("Saindo... Obrigado por utilizar nosso controlador de acesso!")
            break

        case _:
            print("Opção inválida!")