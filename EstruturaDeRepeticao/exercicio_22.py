'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.
'''

print('Primos de 1 a 1000')
numero = input('Digite um numero inteiro entre 1 e 1000: ')
numero = int(numero)
primos_divisao = {}

if numero <= 1000:

    for n in range(1,1000):
        qtd_divisor = 0
        divisao_primos = []

       fy.g for v in range(1,1000):
            if n % v == 0 :
                qtd_divisor += 1
                divisao_primos.append(v)

        if qtd_divisor == 2:
            primos_divisao[n] = divisao_primos

    if primos_divisao.get(numero):
        print(f'O numero {numero} é primo pois é divisivel por: {primos_divisao.get(numero)}')

    else:
        print(f'O numero {numero}, não é um numero primo!')


else:
    print('Numero digitado é INVALIDO')