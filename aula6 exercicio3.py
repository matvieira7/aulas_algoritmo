'''Crie uma lista com 10 números e mostre apenas os números pares.'''

num = []
for i in range(10):
    valor = int(input(f"Digite o {i+1}º número: "))
    if valor %2 == 0:
        num.append(valor)
print(f"LISTA DOS PARES: {num}")