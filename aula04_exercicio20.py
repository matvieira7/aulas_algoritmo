""" Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5."""

numero = int(input("Digite um número: "))
contador = 0

for i in range(1, numero + 1):
    if i % 3 == 0 or i % 5 == 0:
        contador += 1

print(f"Entre 1 e {numero}, {contador} números são múltiplos de 3 ou 5.")