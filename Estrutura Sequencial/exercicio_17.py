'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de
tinta a serem compradas e os respectivos preços em 3 situações:

    A.comprar apenas latas de 18 litros;
    B.comprar apenas galões de 3,6 litros;
    C.misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
      arredonde os valores para cima, isto é, considere latas cheias.

'''
import math

metros_pintar = float(input('Digite a quantidade de metros que deseja pintar: '))

desempenho_galao = 3.6 * 6
desempenho_lata = 18 * 6

desejo =  input('Deseja comprar somente latas(S/N): ')

if desejo == 's':

    qtd_lata = metros_pintar/desempenho_lata
    preco = math.ceil(qtd_lata)*80
    print('Comprar {} latas de tinta, no valor de R${} !'.format(math.ceil(qtd_lata),
                                                                 preco))

elif desejo == 'n':

    desejo = input('Deseja comprar apenas Galões(S/N): ')

    if desejo == 's':

        qtd_galao = metros_pintar/desempenho_galao
        preco = math.ceil(qtd_galao)*25

        print('Comprar {} Galões de tinta, no valor de R${} !'.format(math.ceil(qtd_galao),
                                                                      preco))

    elif desejo == 'n':

        qtd_lata = metros_pintar//desempenho_lata
        qtd_galao = (metros_pintar%desempenho_lata)/desempenho_galao
        preco_lata = qtd_lata*80
        preco_galao = math.ceil(qtd_galao)*25

        print('Comprar {} Latas de tinta, no valor de R${} \n'
              'Comprar {} Galões de tinta, no valor de R${} '.format(math.ceil(qtd_lata),
                                                                     preco_lata,
                                                                     math.ceil(qtd_galao),
                                                                     preco_galao))

    else:
        print('Valor digitado é invalido, por favor digite S ou N !')
