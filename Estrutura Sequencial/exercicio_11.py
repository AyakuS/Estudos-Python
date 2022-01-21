'''

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.

'''

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um outro numero inteiro: '))
n3 = float(input('Digite um numero real: '))

print('a. O produto do dobro do primeiro com metade do segundo .')
quest_a = (n1**2)+n2/2
print('Resultado de A: {}'.format(quest_a))
print('b. a soma do triplo do primeiro com o terceiro.')
quest_b = n1**3+n3
print('Resultado B: {}'.format(quest_b))
print('c. o terceiro elevado ao cubo')
quest_c = n3**3
print('Resultado C: {}'.format(quest_c))