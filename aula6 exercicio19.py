'''Simule um carrinho de compras: adicione produtos até que o usuário digite 'fim' e, no final, mostre o carrinho.'''

carrinho = []

while True:
    produto = input("Adicione um produto ao carrinho (ou digite 'fim' para encerrar): ")
    if produto == 'fim':
        break
    carrinho.append(produto)

print("Produtos no carrinho:")
for item in carrinho:
    print(f"- {item}")
