'''Crie uma lista com 5 strings e conte quantas começam com a letra 'A'.'''

lista = ["Ana", "alberto", "Bruno", "Amanda", "Carlos"]

contador = 0

for palavra in lista:
    if palavra.lower().startswith('a'):
        contador += 1

print(f"Na lista {contador} palavras começam com a letra A.")