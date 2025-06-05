'''Encontre o maior e o menor elemento de uma matriz.'''

matriz = [
    [3, 7, 1],
    [9, 5, 2],
    [4, 8, 6]
]

maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento

print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")