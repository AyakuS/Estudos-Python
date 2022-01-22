"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.
"""
while True:
    inteiro = int(input("Digite um numero inteiro: "))
    divisor = 0
    primos = 0

    while divisor < inteiro:
        divisor += 1
        if inteiro % divisor == 0:
            primos += 1


    if primos == 2:
        print(f"O numero {inteiro} é primo! ")
    else:
        print(f"O numero {inteiro} não é primo!\n")

    print("Deseja saber outro numero?")
    opcao = input()
    if opcao.upper() == "S":
        continue
    else:
        break