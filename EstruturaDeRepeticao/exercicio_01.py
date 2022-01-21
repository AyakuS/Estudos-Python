'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
'''

condicao = True
while condicao:

    numero = int(input('Digite um numero entre 0 e 10: '))

    if numero >= 0  and numero <=10:

        print('O valor digitado é valido!')
        condicao = False
    else:
        print('Digite um valor de valido entre 0 e 10!\n')
