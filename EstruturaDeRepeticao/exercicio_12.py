'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
'''

condicao = True
while condicao:
    multiplicador = int(input('Digite qual tabuda(somente do 1 ao 10) deseja saber:  '))

    if multiplicador >= 1 and multiplicador <= 10: # Validação da tabuada

        for n in range(1,11,1): # Laço que faz a multiplicação
            tabuada  = multiplicador * n
            print(f'{multiplicador} X {n} = {tabuada}')

    deseja = str.upper(input('Deseja Continuar? S/N'))
    if deseja == 'S':
        condicao = True
    elif deseja == 'N':
        condicao = False
    else:
        print('Digite o valor valido! Programa Reiniciado !')
        print('\n')
else:
        print('Digite a tabudada do 1 ao 10 !')