'''Crie uma matriz 3x3 com valores digitados pelo usuário.'''

linhas = 3
colunas = 3
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz resultante:")

for linha in matriz:
    print(linha)