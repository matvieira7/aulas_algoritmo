'''Faça um programa que leia uma matriz 4x4 e diga quantos elementos estão acima da média.'''

matriz = []
soma = 0

for i in range(4):
    linha = []
    for j in range(4):
        valor = float(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)

total_elementos = 4 * 4
media = soma / total_elementos
acima_da_media = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > media:
            acima_da_media += 1

print(f"\nA média dos elementos é: {media}")
print(f"Quantidade de elementos acima da média: {acima_da_media}")
