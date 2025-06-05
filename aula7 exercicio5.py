'''Conte quantos números pares existem em uma matriz.'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pares = 0

for linha in matriz:
    for num in linha:
        if num % 2 == 0:
            pares += 1

print(f"Quantidade de números pares: {pares}")