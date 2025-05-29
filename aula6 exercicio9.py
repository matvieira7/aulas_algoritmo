'''Crie uma lista com 5 notas de alunos, calcule a média e diga quais alunos ficaram acima da média.'''

alunos = ["Lucas", "Ana", "Bruno", "Fernanda", "Mateus"]
aprovados = []
notas = []

for i in range(5):
    nota = int(input(f"Digite a nota do aluno {alunos[i]}: "))
    notas.append(nota)
    if nota >= 6:
        aprovados.append(alunos[i])

print(f"A media foi de {(sum(notas)) / 3}")
print(f"Alunos aprovados: {aprovados}")