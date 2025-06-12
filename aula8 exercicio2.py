'''Crie uma função que receba dois números e retorne a média entre eles.'''

def calcular_media():
    n1 = int(input("Digite o 1 numero: "))
    n2 = int(input("Digitee o 2 numero: "))
    return (n1 + n2) / 2

print(f"a media deles é: {calcular_media()}")