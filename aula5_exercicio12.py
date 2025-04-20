"""O Sistema define um estoque inicial de produtos e a cada venda, retira quantidade do estoque. O sistema encerra quando não permite vender mais do que o disponível."""

estoque = 10
print(f"Estoque inicial: {estoque} unidades.")

while estoque > 0:
    try:
        venda = int(input("Quantas unidades deseja vender: "))
        if venda <= 0:
            print("Venda inválida.")
        elif venda <= estoque:
            estoque -= venda
            print(f"Venda realizada! Estoque restante: {estoque}")
        else:
            print("Não há estoque suficiente para essa venda.")
    except ValueError:
        print("Digite um número inteiro válido.")

print("Estoque zerado. Sistema encerrado.")