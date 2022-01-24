"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
1 e um número inteiro informado pelo usuário.
"""

while True:
    inteiro = int(input("Digite um numero inteiro: "))
    divisor = 1
    primos = []

    for n in range(1, inteiro+1):
        vdd = 0
        for i in range(1, inteiro+1):
            if n % i == 0:
                vdd += 1
        if vdd == 2:
            primos.append(n)

    print(f"Os numeros primos: {primos}")
    print("Deseja saber outro numero?")
    opcao = input()

    if opcao.upper() == "S":
        continue
    elif opcao.upper() == "N":
        break
    else:
        print("Valor ")

