''''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1
'''
print('Primos de 1 a 1000')
numero = input('Digite um numero inteiro entre 1 e 1000: ')
numero = int(numero)
lista = []
primo = 0
if numero <= 1000:

    for n in range(1,1000):
        qtd_divisor = 0
        for v in range(1,1000):
            if n % v == 0 :
                qtd_divisor += 1
        if qtd_divisor == 2:
            lista.append(n)
    for n in lista:
        if n == numero:
           primo = numero

    if primo > 0 :
        print(f'O numero {numero}, pertence aos numeros primos!')
    else:
        print(f'O numero {numero}, não pertence aos numeros primos!')
else:
    print('Numero digitado é INVALIDO')