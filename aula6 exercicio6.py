'''Verifique se um nome digitado pelo usuário está em uma lista de nomes.'''

lista = ["Lucas", "Ana", "Bruno", "Fernanda", "Mateus", "Juliana", "Carlos", "Sofia", "Rafael", "Beatriz"]

while True:
    nomes = input("Digite um nome: ")
    if nomes.strip().capitalize() in lista:
        print("O nome digitado está na lista!")
        break
    else:
        print("O nome digitado não esta na lista, tente outro")