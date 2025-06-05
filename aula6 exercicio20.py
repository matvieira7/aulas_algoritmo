'''Desenvolva um menu de opções para gerenciar uma lista de tarefas: adicionar, remover, exibir e sair.'''

tarefas = []

while True:
    print("\Menu:")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Exibir tarefas")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        tarefa = input("Digite a tarefa para adicionar: ")
        tarefas.append(tarefa)
    elif opcao == 2:
        tarefa = input("Digite a tarefa para remover: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida.")
        else:
            print("Tarefa não encontrada.")
    elif opcao == 3:
        print("Lista de tarefas:")
        for t in tarefas:
            print(f"- {t}")
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente um numero de 1 a 43")
