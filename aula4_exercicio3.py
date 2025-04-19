""" Faça um programa que solicite 5 notas e calcule a média."""

soma = 0
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 5
print(f"A média dos números digitados é {media:.2f}")