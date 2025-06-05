'''Crie uma matriz identidade 4x4.'''

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for l in matriz:
    print(l)