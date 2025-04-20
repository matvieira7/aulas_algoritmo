"""Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) e calcule a média dessas notas. O programa deve parar quando o usuário digitar uma nota negativa."""

soma = 0
contador = 0

while True:
    entrada = input("Digite uma nota de 0 a 10 (ou um número negativo para sair): ")

    try:
        nota = float(entrada)

        if nota < 0:
            print("Encerrando o programa...")
            break
        elif 0 <= nota <= 10:
            soma += nota
            contador += 1
            media = soma / contador
            print(f"Nota registrada com sucesso. Média atual: {media:.2f}")
        else:
            print("Nota fora do intervalo permitido. Digite entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite apenas números de 0 a 10 ou um número negativo para sair.")

if contador > 0:
    print(f"\nVocê inseriu {contador} notas.")
    print(f"Média final: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
