'''Crie uma função que receba uma lista de números e retorne quantos são pares.'''

def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

numeros = [1, 4, 7, 8, 10, 3, 2]
quantidade_pares = contar_pares(numeros)
print(f"Números pares: {quantidade_pares}")