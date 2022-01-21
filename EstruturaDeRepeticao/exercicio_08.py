'''

Faça um programa que leia 5 números e informe a soma e a média dos números.

'''
soma = 0
for n in range(1,6,1):
    numero = int(input(f'Digite a n{n}: '))
    soma = soma + numero

media = soma/5
print(f'media = {media}')