"""1. Conversor de Moedas
Implemente um conversor de moedas que permita ao usuário escolher entre Dólar (USD), Euro (EUR) e Libra (GBP) e converter um valor informado para Reais (BRL)."""

quantia = float(input("Diga a quantia desejável para conversão: "))

while True:
    print("\n===== CONVERSOR DE MOEDAS =====")
    print("1 - Dólar (USD)")
    print("2 - Euro (EUR)")
    print("3 - Libra (GBP)")
    print("4 - Sair")

    opcao = input("Escolha o numero de uma moeda: ")

    match opcao:
        case "1":
            conta = quantia * 5.73
            print(f"Sua conversão atual é R$ {conta:.2f}")

        case "2":
            conta = quantia * 6.18
            print(f"Sua conversão atual é R$ {conta:.2f}")

        case "3":
            conta = quantia * 7.38
            print(f"Sua conversão atual é R$ {conta:.2f}")

        case "4":
            print("Saindo... Obrigado por utilizar nosso conversor de moedas!")
            break

        case _:
            print("Opção inválida!")