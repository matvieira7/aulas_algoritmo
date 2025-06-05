'''Substitua todos os números ímpares de uma lista por zero.'''

import random

lista = [random.randint(0, 10) for _ in range(10)]

print(f"{lista}")

for i in range(len(lista)):
    if lista[i] % 2 != 0:
        lista[i] = 0
print(f"{lista}")