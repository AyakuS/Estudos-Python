'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''


numero = input('Digite a quantidade de numeros primos: ')
numero = int(numero)
primos_divisao = {}

for n in range(1,numero):

    qtd_divisor = 0
    divisao_primos = []

    for v in range(1,numero):
        qtd_divisoes = 0
        if n % v == 0 :
           qtd_divisor += 1
           divisao_primos.append(v)

    if qtd_divisor == 2:
        primos_divisao[n] = divisao_primos

for i in primos_divisao:
    print(f'Primos: {i} = {primos_divisao.get(i)} ; Quantidade de divisões {numero}')