soma_par = 0
soma_impar = 0
cont_impar = 0
inicio = int(input("Digite o inicio:"))
fim = int(input("Digite o fim:"))

for i in range(inicio, fim):
    #print(i)

    if i % 2 == 0:
        print(f"{i} = PAR")
        soma_par += i
    else:
        print(f"{i} = IMPAR")
        soma_impar += i
        cont_impar += 1
        media = soma_impar / cont_impar
print(f"Soma dos pares = {soma_par}")
print(f"Soma dos impares = {soma_impar}")
print(f"Qtd de impares = {cont_impar}")
print(f"Média dos numeros impares = {media}")