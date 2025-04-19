"""Solicite ao usuário um número e verifique se ele é par ou ímpar.

Se o número for par, divida-o por 2 e exiba o resultado.

Se o número for ímpar, multiplique-o por 3 e exiba o resultado."""

numero = int(input("Digite um numero:"))

if numero %2 == 0:
    numero /= 2
    print(numero)
else:
    numero *= 3
    print(numero)