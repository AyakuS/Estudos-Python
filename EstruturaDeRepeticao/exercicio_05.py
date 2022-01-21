'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação
'''

a = float(input('Digite a quantidade de Habitantes do primeiro pais: '))
b = float(input('Digite a quantidade de Habitantes do segundo pais: '))
taxa_a = int(input('Digite o percentual de descrimento do primeiro pais: '))
taxa_b = int(input('Digite o percentual de descrimento do segundo pais: '))
anos = 0
if a < b:
    while a < b:
        anos += 1
        a = a + (a*(taxa_a/100))
        b = b + (b*(taxa_b/100))
    print(f'Anos: {anos}')
    print(' Pais A: {:.0f} , Pais B: {:.0f}'.format(a, b))
else:
    while b < a:
        anos += 1
        a = a + (a*(taxa_a/100))
        b = b + (b*(taxa_b/100))
    print(f'Anos: {anos}')
    print(' Pais B: {:.0f} , Pais A: {:.0f}'.format(b, a))
