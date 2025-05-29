'''Faça um programa que leia 10 números e armazene em duas listas: uma com pares e outra com ímpares.'''

pares = []
impares = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º número: "))
    if valor %2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f"LISTA DOS PARES: {pares}")
print(f"LISTA DOS IMPARES: {impares}")