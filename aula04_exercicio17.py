"""Peça um número ao usuário e some separadamente os pares e os ímpares de 1 até esse número."""

numero = int(input("Digite um número para ver a soma de pares e ímpares dele: "))

soma_pares = 0
soma_impares = 0

print("SOMA DOS PARES")
for i in range (0,numero + 1, 2):
         soma_pares += i
         print(f"Somando {i} -> Total parcial: {soma_pares}")
print("-----------------------------------------------------------------------------------")
print("SOMA DOS ÍMPARES")
for i in range (1,numero + 1, 2):
         soma_impares += i
         print(f"Somando {i} -> Total parcial: {soma_impares}")