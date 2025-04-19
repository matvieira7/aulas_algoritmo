"""Solicite um número ao usuário e exiba o seu fatorial (n!)."""

numero = int(input("Digite um número para ver o fatorial: "))
n = 0

for i in range(numero, 10):
    n = i*i
    print(f"{i} X {i} = {n}")