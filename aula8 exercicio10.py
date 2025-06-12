'''Crie um menu com funções para:
Cadastrar nomes
Listar nomes
Sair do programa'''

def cadastrar_nome(lista):
    nome = input("Digite o nome para cadastrar: ")
    lista.append(nome)
    print(f"Nome '{nome}' cadastrado com sucesso!\n")

def listar_nomes(lista):
    if len(lista) == 0:
        print("Nenhum nome cadastrado.\n")
    else:
        print("Nomes cadastrados:")
        for i, nome in enumerate(lista, start=1):
            print(f"{i}. {nome}")
        print()

def menu():
    nomes = []
    while True:
        print("MENU:")
        print("1 - Cadastrar nome")
        print("2 - Listar nomes")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_nome(nomes)
        elif opcao == "2":
            listar_nomes(nomes)
        elif opcao == "3":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()