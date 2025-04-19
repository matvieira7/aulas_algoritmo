"""Peça ao usuário um número e exiba a tabuada desse número de 1 a 10."""

numero = int(input("Digite um número para ver a tabuada dele: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")