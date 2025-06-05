'''Verifique se duas matrizes 2x2 digitadas pelo usuário são iguais.'''

matriz1 = []
matriz2 = []

print("Digite os valores da primeira matriz 2x2:")

for i in range(2):
    linha = []

    for j in range(2):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz1.append(linha)

print("\nDigite os valores da segunda matriz 2x2:")

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz2.append(linha)

iguais = True

for i in range(2):
    for j in range(2):
        if matriz1[i][j] != matriz2[i][j]:
            iguais = False

if iguais:
    print("As matrizes são IGUAIS!")
else:
    print("As matrizes são DIFERENTES!")