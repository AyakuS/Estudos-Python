'''
Altere o programa anterior para mostrar no final a soma dos números.
'''
n1 = int(input('Digite o numero: '))
n2 = int(input('Digite outro numero: '))
soma = 0
if n1 > n2:

    while n1 > n2:
        x = n2
        n2 += 1
        if soma > x :
            soma = soma + n2
        else:
            soma = x + n2

    print(f'Soma = {soma}')

elif n2 > n1:
    while n2 > n1:
        x = n1
        n1 += 1
        if soma > x:
            soma = soma + n1
        else:
            soma = x + n1

    print(f'Soma = {soma}')