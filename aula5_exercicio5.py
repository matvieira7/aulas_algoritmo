"""Crie um programa que simule um caixa eletrônico, que continue pedindo ao usuário para inserir um valor de saque até que o saldo da conta seja zero ou negativo."""

saldo = float(input("Digite o saldo da sua conta R$:"))

while saldo > 0:
    saque = float(input("Digite o valor de saque para retirar R$:"))
    saldo -= saque
    print(f"Sua conta ainda tem R$:{saldo} se chegar a 0 vocÊ não poderá mais sacar e se passar de 0 você ficará devendo o banco então CUIDADO!")