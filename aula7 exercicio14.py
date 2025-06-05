'''Multiplique todos os elementos de uma matriz por um número dado pelo usuário.'''

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

multiplicador = int(input("Digite o número para multiplicar a matriz: "))

for i in range(3):
    for j in range(3):
        matriz[i][j] *= multiplicador

print("\nMatriz após multiplicação:")

for linha in matriz:
    print(linha)