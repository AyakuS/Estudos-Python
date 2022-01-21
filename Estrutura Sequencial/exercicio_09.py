'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
calculo: C = 5 * ((F-32) / 9
'''
f = int(input('Digite a temperatura em Fahrenheit: '))
c = 5 * ((f-32)/9)
print('A temperatura em Celsius é: {:.0f}º'.format(c))
