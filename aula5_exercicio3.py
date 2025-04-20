positivos = 0
negativos = 0
zeros = 0

while True:
    numero = input("Digite um número ou 'sair' para sair: ")
    if numero == "sair":
        break
    try:
        numero = int(numero)
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1
    except ValueError:
        print("Entrada inválida. Digite um número ou 'sair'.")

print(f"Você digitou um total de {positivos} números positivos.")
print(f"Você digitou um total de {negativos} números negativos.")
print(f"Você digitou um total de {zeros} zeros.")
