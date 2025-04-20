"""Crie um programa que solicite ao usuário para inserir números e some esses números até que o usuário insira zero. Quando zero for inserido, o programa deve imprimir a soma total."""

soma = 0
numero = int(input("Digite um numero para somar! E (0) para sair: "))

while numero != 0:
    soma += numero
    numero = int(input("Digite mais um numero: "))

print("Soma Total: ", soma)