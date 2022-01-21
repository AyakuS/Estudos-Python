'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
'''

base = int(input('Digite a Base: '))
expoente = int(input('Digite o Expoente: '))
n = 0
potencia = 0

while n < (expoente - 1):
    n += 1

    if potencia > 0:
        potencia = potencia * base


    elif expoente == 2:
        potencia = base * base

    else:
        potencia = base * base


print(f'Potencia : {potencia}')