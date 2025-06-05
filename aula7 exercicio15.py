'''Troque os valores da primeira linha com a última linha de uma matriz.'''

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

matriz[0], matriz[-1] = matriz[-1], matriz[0]

print("\nMatriz após trocar a primeira e última linha:")

for linha in matriz:
    print(linha)