'''Faça uma função que recebe uma lista e retorna outra com os elementos em ordem reversa (sem usar .reverse() ou [::-1]).'''

def inverter_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

lista = [1, 2, 3, 4, 5]
print(inverter_lista(lista))
