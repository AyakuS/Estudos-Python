'''

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

'''

fat = int(input('Qual fatorial quer saber?: '))
aux = fat
fatorial = 0

for n in range(1,fat,1):

    if aux == fat:
        aux = aux - 1
        fatorial = fat * aux
    else:
        aux = aux - 1
        fatorial = fatorial * aux


