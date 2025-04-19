"""Peça ao usuário um número e exiba uma contagem de 1 até esse número."""

incremento = int(input("Digite até onde vai a contagem: "))
for i in range(1, incremento, 1):
    print(i)
print(incremento)