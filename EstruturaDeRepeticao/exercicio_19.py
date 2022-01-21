'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
'''
conjunto = int(input('Digite a Quantidade de N do conjunto: '))
lista = []
if conjunto <= 1000:
    for n in range(1,conjunto+1,1):
        add = lista.append(int(input(f'Digite o {n} conjunto: ')))

    menor = lista[0]
    maior = lista[0]
    soma = 0
    for n in lista: # Laço de menor/maior/soma valor !

        if n < menor:
            menor = n
        if n > maior:
            maior = n
        if soma == 0 :
            soma = n
        else:
            soma = soma + n

    print(f'Menor valor: {menor}, Maior valor: {maior} e Soma do conjunto: {soma}')
else:
    print('Digite um valor valido, entre 0 e 1000 ! ')