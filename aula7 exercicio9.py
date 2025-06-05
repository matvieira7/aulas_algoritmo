'''Some os elementos de cada coluna de uma matriz e mostre os resultados.'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_colunas = len(matriz[0])

for j in range(num_colunas):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][j]
    print(f"Soma da coluna {j+1}: {soma}")