""" Peça um número ao usuário e exiba sua tabuada de 1 a 10, mas se for múltiplo de 3, substitua pelo texto "Multiplo de 3"."""

numero = int(input("Digite um número para ver a tabuada dele ou se é múltiplo de 3: "))

if numero % 3 == 0:
    print(f"{numero} é múltiplo de 3.")
else:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")