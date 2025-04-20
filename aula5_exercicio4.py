"""Faça um programa que converta uma temperatura de Celsius para Fahrenheit. Continue pedindo ao usuário para inserir uma nova temperatura em Celsius até que ele digite "sair"."""

temperatura = input("Digite a temperatura em Celsius para converter em Fahrenheit! E ""sair"" para sair: ")

while True:
    if temperatura == "sair":
        break

    try:
        temperatura = float(temperatura)
        fahrenheit = (temperatura * 9 / 5) + 32
        print(f"{temperatura}°C é igual a {fahrenheit:.2f}°F")

    except ValueError:
        print("Entrada inválida. Digite um número ou 'sair'.")

        temperatura = input("Digite a temperatura em Celsius para converter em Fahrenheit! ou ""sair"" para sair: ")