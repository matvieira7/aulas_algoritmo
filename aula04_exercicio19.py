"""Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero."""

positivos = 0
negativos = 0
zeros = 0

for i in range(1, 11, 1):
    try:
        numero = int(input(f"Digite o {i}° numero:"))
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1
    except ValueError:
        print("Erro. Insira um número inteiro!")
        i -= 1

print(f"dos 10 numeros digitados {positivos} são positivos.")
print(f"dos 10 numeros digitados {negativos} são negativos.")
print(f"dos 10 numeros digitados {zeros} são zeros.")