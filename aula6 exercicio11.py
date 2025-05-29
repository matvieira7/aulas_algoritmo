'''Remova todos os números negativos de uma lista de inteiros.'''

import random

lista = [random.randint(-10, 10) for _ in range(10)]
i = 0

print(f"{lista}")

while i < len(lista):
    if lista[i] < 0:
        lista.remove(lista[i])
    else:
        i += 1

print(f"{lista}")
