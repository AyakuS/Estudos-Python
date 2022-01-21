'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58

'''
altura = float(input('Digite seu altura: '))
imc = (72.7*altura)-58
print('Seu IMC é de {:.2f} !'.format(imc))