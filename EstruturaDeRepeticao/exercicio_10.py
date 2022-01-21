'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles
'''

n1 = int(input('Digite o numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    while n1 >= n2:
        print(n2)
        n2+=1


elif n2 > n1:
    while n2 >= n1:
        print(n1)
        n1+=1