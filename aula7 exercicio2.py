'''Some todos os elementos de uma matriz 3x3.'''

linhas = 3
colunas = 3
matriz = []
soma = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        soma += valor
        linha.append(valor)
    matriz.append(linha)

print("Matriz resultante:")

for linha in matriz:
    print(linha)
print(f"Soma de todos os valores da matriz: {soma}")