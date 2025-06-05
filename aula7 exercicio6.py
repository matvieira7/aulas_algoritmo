'''Calcule a média de todos os elementos de uma matriz.'''

linhas = 3
colunas = 3
matriz = []
soma = 0
media = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        media +=1
        soma += valor
        linha.append(valor)
    matriz.append(linha)

print("Matriz resultante:")

for linha in matriz:
    print(linha)
print(f"Soma de todos os valores da matriz: {soma}")
print(f"Média dos valores da matriz: {soma/media}")