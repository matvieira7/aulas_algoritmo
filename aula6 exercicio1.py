'''Crie uma lista com 5 números inteiros e exiba cada número ao quadrado.'''

num = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º número: "))
    valor *= valor
    num.append(valor)
print(num)