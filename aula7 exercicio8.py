'''Some os elementos de cada linha de uma matriz e mostre os resultados.'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
    print(f"Soma da linha {i+1}: {soma}")