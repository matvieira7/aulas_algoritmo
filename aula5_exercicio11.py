"""O usuário digita o preço e a quantidade de produtos até digitar “sair”. O Sistema mostra a quantidade de produtos e o valor final da compra."""

total = 0
quantidade_total = 0

print("Digite o preço e a quantidade dos produtos. Digite 'sair' para encerrar.")

while True:
    preco = input("Preço do produto: ")
    if preco.lower() == "sair":
        break

    quantidade = input("Quantidade: ")
    if quantidade.lower() == "sair":
        break

    try:
        preco = float(preco)
        quantidade = int(quantidade)
        total += preco * quantidade
        quantidade_total += quantidade
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")

print(f"\nVocê comprou {quantidade_total} produtos.")
print(f"Valor total da compra: R$ {total:.2f}")
