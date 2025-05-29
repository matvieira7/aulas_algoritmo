'''Faça um programa que leia números do usuário até que ele digite 0. Depois, mostre a lista e a soma dos números.'''

numeros = []
while True:
    num = int(input("Digite um numero ou 0 para sair: "))
    if num == 0:
        break
    else:
        numeros.append(num)
total = sum(numeros)
print(f"{numeros}")
print(f"Soma dos numeros digitados: {total}")