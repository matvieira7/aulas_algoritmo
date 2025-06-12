'''Crie uma função converter_para_fahrenheit(celsius) que converta graus Celsius para Fahrenheit.'''

def converter_para_fahrenheit():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")

converter_para_fahrenheit()