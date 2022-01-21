'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
a números inteiros positivos e menores que 16.
'''
condicao = True
while condicao == True:

    fat = int(input('Qual fatorial quer saber?: '))
    aux = fat
    fatorial = 0

    if fat > 0 and fat <= 16:

        for n in range(1, fat, 1):

            if aux == fat:
                aux = aux - 1
                fatorial = fat * aux
            else:
                aux = aux - 1
                fatorial = fatorial * aux
        print(f'Valor do fatorial: {fatorial}')

        deseja = str.upper(input('Deseja continuar? S/N: '))

        if deseja == 'S':
            condicao = True
        elif deseja == 'N':
            condicao = False


    else:
        print('Digite numeros inteiros positivos e menores que 16 ! Programa será reiniciado!')
