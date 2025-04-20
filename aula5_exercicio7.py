"""Crie um programa que converta uma quantia em dólares para euros. Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0"."""

dolares = float(input("Digite o valor em dolares para converter em euros! E (0) para sair: "))

while dolares != 0:
        euros = dolares * 0.88
        print(f"{dolares} dolares é igual a {euros:.2f} euros")

        dolares = float(input("Digite o valor em dolares para converter em euros! E (0) para sair: "))