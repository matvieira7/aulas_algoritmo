'''Leia uma lista de números e crie uma nova lista apenas com os valores únicos (sem repetições).'''

numeros = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7, 8]

unicos = []

for num in numeros:
    if num not in unicos:
        unicos.append(num)

print(f"{numeros}")
print(f"{unicos}")
