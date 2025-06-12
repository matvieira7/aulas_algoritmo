'''Desafio Final (Avançado)
Simule um sistema de cadastro de produtos com as seguintes opções:

1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto pelo nome
4 - Sair
Use uma lista para armazenar os produtos.
Crie funções para cada opção.
Utilize laços de repetição e estruturas de decisão junto com funções.'''

def cadastrar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    produto = {"nome": nome, "preco": preco}
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!\n")

def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.\n")
    else:
        print("Produtos cadastrados:")
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto['nome']} - R${produto['preco']:.2f}")
        print()

def buscar_produto(produtos):
    busca = input("Digite o nome do produto para buscar: ").lower()
    encontrados = []
    for produto in produtos:
        if busca in produto["nome"].lower():
            encontrados.append(produto)

    if len(encontrados) == 0:
        print("Produto não encontrado.\n")
    else:
        print("Produtos encontrados:")
        for produto in encontrados:
            print(f"- {produto['nome']} - R${produto['preco']:.2f}")
        print()

def exibir_menu():
    print("===== Sistema de Cadastro de Produtos =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto pelo nome")
    print("4 - Sair")

def main():
    produtos = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            buscar_produto(produtos)
        elif opcao == "4":
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()