'''Crie uma função valida_idade(idade) que retorne se a pessoa é maior de idade.'''

def valida_idade():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

valida_idade()