""" Faça um controle de estoque com menu de entrada, saída e exibição."""

estoque = {}

while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1. Entrada de Produto")
    print("2. Saída de Produto")
    print("3. Exibir Estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Nome do produto para entrada: ").strip().lower()
        try:
            quantidade = int(input("Quantidade a adicionar: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
                continue
        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
        print(f"{quantidade} unidades de '{produto}' adicionadas ao estoque.")

    elif opcao == "2":
        produto = input("Nome do produto para saída: ").strip().lower()
        if produto not in estoque:
            print("Esse produto não existe no estoque.")
            continue
        try:
            quantidade = int(input("Quantidade a retirar: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
                continue
        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        if quantidade > estoque[produto]:
            print("Não há essa quantidade em estoque.")
        else:
            estoque[produto] -= quantidade
            print(f"{quantidade} unidades de '{produto}' removidas do estoque.")
            if estoque[produto] == 0:
                del estoque[produto]  # remove se zerar o produto

    elif opcao == "3":
        if not estoque:
            print("Estoque vazio.")
        else:
            print("\n📋 Estoque Atual:")
            for produto, qtd in estoque.items():
                print(f"- {produto}: {qtd} unidade(s)")

    elif opcao == "4":
        print("Encerrando o sistema de estoque...")
        break

    else:
        print("Opção inválida. Tente novamente.")
