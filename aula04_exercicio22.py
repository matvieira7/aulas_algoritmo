"""O computador escolhe um número aleatório de 1 a 10, e o usuário tem 3 tentativas para adivinhar. Dê dicas se o número é maior ou menor."""

import random

numero_secreto = random.randint(1, 10)

print("TENTE ADVINHAR O NUMERO DE 1 A 10 EM 3 TENTATIVAS!!!")

for i in range(1, 4, 1):
    palpite = int(input(f"Palpite de numero{i}:"))
    if palpite == numero_secreto:
        print("PARABÉNS! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("Dica: O número é MAIOR.")
    else:
        print("Dica: O número é MENOR.")

    if i == 3:
        print(f"\nSuas tentativas acabaram! O número era {numero_secreto}.")