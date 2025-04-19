"""Peça um número ao usuário e some seus dígitos (exemplo: 123 → 1+2+3 = 6)."""

numero = input("Digite um número: ")
soma = 0

for digito in numero:
    soma += int(digito)

print("A soma dos dígitos é:", soma)
