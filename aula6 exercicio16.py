'''Junte duas listas e remova os elementos repetidos.'''

lista1 = [1, 2, 3, 5, 7]
lista2 = [1, 2, 3, 4, 7]

lista_junta = lista1 + lista2

lista_sem_repetidos = []
for item in lista_junta:
    if item not in lista_sem_repetidos:
        lista_sem_repetidos.append(item)

print(f"{lista_sem_repetidos}")