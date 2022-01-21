"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

cd = int(input('Digite o tamanho da sua coleção de CD: '))
count = 0
valor_total = 0
while count < cd:
    count += 1
    valor = int(input(f'Digite o valor do CD {count}: '))
    valor_total += valor
media_cd = valor_total/cd

print(f'Valor médio de cada CD é de R${media_cd:.2f}')

