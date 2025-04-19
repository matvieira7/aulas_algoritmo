""" Peça ao usuário para digitar 5 números e exiba o maior e o menor deles."""

maior = None
menor = None

for i in range(1, 6, 1):
    numero = int(input(f"Digite o {i}° numero:"))
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print(f"o numero maior é: {maior}.")
print(f"o numero menor é: {menor}.")