'''Crie uma função calcular_desconto(valor, percentual=10) que aplique um desconto percentual ao valor.'''

def calcular_desconto():
    valor = float(input("Digite o valor do produto: R$ "))
    percentual = float(input("Digite o percentual de desconto (pressione Enter para usar 10%): ") or 10)

    desconto = valor * (percentual / 100)
    valor_final = valor - desconto

    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor com desconto: R$ {valor_final:.2f}")

calcular_desconto()