'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números
impares
'''
lista = []
par, impar  = 0, 0

for n in range(10):
    add = lista.append(int(input(f'Digite dez numeros {n}: ')))


for n in range(10):
    if lista[n] % 2 == 0:
        par += 1
    elif lista[n] % 2 == 1:
        impar += 1

print(f'Quantidade de numeros Pares: {par}\n'
      f'Quantidade de numeros Impares: {impar}')

