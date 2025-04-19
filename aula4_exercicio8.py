"""Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente."""

numero = int(input("Digite um número para iniciar a contagem: "))
incremento = int(input("Digite até onde vai essa contagem: "))
passo = int(input("Digite de quanto em quanto essa contagem vai andar: "))

for i in range(numero, incremento, passo):
    print(i)
print(incremento)