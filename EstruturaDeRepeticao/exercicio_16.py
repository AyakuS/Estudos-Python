'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
valor seja maior que 500.
'''
n = 500
ultimo = 0
penultimo = 1


if (n == 1) or (n == 2):
    print(1)
else:
    print(ultimo)
    print(penultimo)
    count = 3

    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(f'O N-ésimo termo é: {termo}')


