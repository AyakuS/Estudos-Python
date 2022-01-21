'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
'''
h = float(input('Digite seu altura: '))
imc_h = (72.7*h)-58
imc_m = ((62.1*h) - 44.7)
print('IMC Masculino é {:.2f} para a altura de {} '.format(imc_h, h))
print('IMC Feminino é {:.2f} para a altura de {}'.format(imc_m, h))
