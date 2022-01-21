'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
    A.salário bruto.
    B.quanto pagou ao INSS.
    C.quanto pagou ao sindicato.
    D.o salário líquido.
    E.calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''
salario_hr = float(input('Digite seu salário: '))
qtd_hr_trabalhada = float(input('Digite a carga horaria: '))
salario_bruto = salario_hr * qtd_hr_trabalhada
irrf = salario_bruto*0.11
sindicato = salario_bruto * 0.05
inss = salario_bruto * 0.08
salario_lqd = salario_bruto - irrf - inss - sindicato
print('Salario Bruto R${:.2f}'.format(salario_bruto))
print('Desconto INSS R${:.2f}'.format(inss))
print('Desconto Sindicato R${:.2f}'.format(sindicato))
print('Salario Liquido R${:.2f}'.format(salario_lqd))
