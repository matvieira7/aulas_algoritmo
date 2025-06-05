'''Conte quantas vezes o número 3 aparece em uma lista.'''

lista = []
while True:
    num = int(input("Digite um numero ou 0 para sair: "))
    if num == 0:
        break
    lista.append(num)
contagem3 = sum(str(num).count("3") for num in lista)
print(f"na lista tem um total de {contagem3} numeros 3")