"""Crie um programa que peça ao usuário para inserir números e encontre o maior número inserido. O programa deve continuar pedindo números até que o usuário digite "sair"."""

maior = 0
numero = int(input("Digite um numero! E (0) para sair: "))

while True:
    numero = int(input("Digite mais um numero: "))
    if numero == 0:
        break
    if numero > maior:
        maior = numero
if maior == 0:
    print("Você não digitou nenhum numero.")
else:
    print(f"O maior numero digitado é: {maior}.")