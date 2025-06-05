'''Leia uma lista de 5 nomes e mostre a lista em ordem alfabética.'''

lista = []
for i in range(5):
    nomes = input(f"Digite o {i+1} nome: ")
    lista.append(nomes)
lista.sort()
print(lista)