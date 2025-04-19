soma = 0

inicio = int(input("Digite o inicio:"))
fim = int(input("Digite o fim:"))
#passo = int(input("Digite o passo:"))

for i in range(inicio, fim):
    print(f"i = {i}")
    soma += i

print(f"Soma = {soma}")