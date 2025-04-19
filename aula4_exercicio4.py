"""Crie um contador que peça ao usuário um número inicial, um número final e um incremento e exiba os valores gerados."""

numero = int(input("Digite um número para iniciar a contagem: "))
incremento = int(input("Digite até onde vai essa contagem: "))

for i in range(numero, incremento, 1):
    print(i)
print(incremento)