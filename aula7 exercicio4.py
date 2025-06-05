'''Mostre os elementos da diagonal secundária de uma matriz quadrada.'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matriz)

print("Elementos da diagonal secundária:")
for i in range(n):
    print(matriz[i][n - 1 - i])