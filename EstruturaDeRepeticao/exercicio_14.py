'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números
impares.

'''
impar, par = 0, 0

for n in range(1,11,1):
    numero = int(input(f'Digite o n{n}:  '))
    if numero % 2 == 0:
        par += 1
    elif numero % 2 == 1:
        impar += 1

print(f'\nQuantidade numeros Impares: {impar}\n'
      f'Quantida de Numeros Pares: {par}')
