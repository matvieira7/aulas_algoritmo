'''Transponha uma matriz 3x3 (trocar linhas por colunas).'''

matriz = []

print("Digite os valores da matriz 3x3:")

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

transposta = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz[j][i])
    transposta.append(linha)

print("\nMatriz Original:")

for linha in matriz:
    print(linha)

print("\nMatriz Transposta:")

for linha in transposta:
    print(linha)