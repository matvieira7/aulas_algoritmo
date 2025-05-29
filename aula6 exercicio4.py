'''Some todos os elementos de uma lista de inteiros digitados pelo usuário.'''

numeros = []
while True:
    num = int(input("Digite um numero ou 0 para sair: "))
    if num == 0:
        break
    else:
        numeros.append(num)
total = sum(numeros)
print(f"Soma dos numeros digitados: {total}")