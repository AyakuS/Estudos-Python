'''
Faça um programa que leia 5 números e informe o maior número.
'''
lista = []

for n in range(5):
    n = lista.append(int(input('Digite um numero: ')))
x = lista[0]
for n in lista:

      if n > x:
          x = n


print(f'o maior numero é: {x}')