"""Faça um programa que permita cadastrar votos para 3 candidatos. Exibe contagem ao final quando for digitado "fim"."""

candidato1 = 0
candidato2 = 0
candidato3 = 0

print("Digite o número do candidato (1, 2 ou 3). Digite 'fim' para encerrar.")

while True:
    voto = input("Seu voto: ").lower()

    if voto == "fim":
        break
    elif voto == "1":
        candidato1 += 1
    elif voto == "2":
        candidato2 += 1
    elif voto == "3":
        candidato3 += 1
    else:
        print("Voto inválido! Tente novamente.")

print("\n--- Resultado da Votação ---")
print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Candidato 3: {candidato3} votos")
