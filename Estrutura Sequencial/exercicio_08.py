'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
'''
salario_hr = float(input('Digite seu salário hora: '))
hr_trabalhada = float(input('Digite as horas trabalhadas: '))

salario_final = salario_hr*hr_trabalhada

print('Há receber: R${}'.format(salario_final))
