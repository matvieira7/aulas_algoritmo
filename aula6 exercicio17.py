'''Faça uma função que recebe uma lista de números e retorna uma nova lista com o fatorial de cada número.'''

lista = [1, 2, 3, 4, 5]  
nova_lista = []

for num in lista:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    nova_lista.append(fatorial)

print(nova_lista)
