"""Solicite um número ao usuário e exiba a soma de 1 até esse número."""

incremento = int(input("Digite um número: "))

for i in range (0, incremento, 1):
    numero = i+1
    print(i,"+ 1 =", numero)