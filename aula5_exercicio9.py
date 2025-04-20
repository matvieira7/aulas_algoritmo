"""Crie um programa que simule a leitura de dados de um sensor e continue capturando dados até que um valor fora do intervalo de operação seja detectado (por exemplo, fora de 0 a 100)."""

registro = 0

while True:
    valor = int(input("Digite o valor do dado do sensor: "))

    if 0 <= valor <= 100:
        print("VALOR REGISTRADO E DENTRO DA OPERAÇÃO")
        registro += 1
    else:
        break  # sai do while se o valor estiver fora do intervalo

print("VALOR FORA DAS OPERAÇÕES")
print(f"Um total de {registro} registros nessa operação")