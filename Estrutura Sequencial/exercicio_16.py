'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total
'''
import math

area_pintar = float(input('Digite o tamanho da área que deseja pintar em metros: '))
desempenho = 3 * 18

if area_pintar <= desempenho:
    print('Comprar Somente uma lata de tinta.')
else:
    qtd_lata = area_pintar/desempenho
    print('Comprar {} latas de tinta ! '.format(math.ceil(qtd_lata)))

