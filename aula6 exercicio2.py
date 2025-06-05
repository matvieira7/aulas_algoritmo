'''Peça ao usuário para digitar 5 nomes e armazene-os em uma lista. Depois, exiba os nomes um por um.'''

lista = []

for i in range(5):
    nomes = input(f"Digite o {i+1} nome: ")
    lista.append(nomes)
    print(f"{nomes} adicionado")
print(f"LISTA DOS NOMES: {lista}")