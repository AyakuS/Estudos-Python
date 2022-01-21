'''
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
'''
condicao = True
while condicao:

    corretas = 0
    nome = str.upper(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    salario = float(input('Digite seu salario: '))
    sexo = str.upper(input('Digite seu sexo F ou M: '))
    estado_civil = str.upper(input('S - Solteiro, C - Casado, V-viuvo, D-Divorciado: '))

    if len(nome) >= 3:
        print(f'Nome: {nome}')
        corretas = corretas + 1
    else:
        print('Nome Invalido !')

    if idade >= 0 and idade <=150:
        print(f'Idade: {idade}')
        corretas = corretas + 1
    else:
        print('Idade Invalida !')

    if salario > 0 :
        print(f'Salario: R${salario}')
        corretas = corretas + 1
    else:
        print('Salario Invalido!')

    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        print(f'Estado Civil: {estado_civil}')
        corretas = corretas + 1
    else:
        print('Estado Civil invalido')

    if sexo == 'F' or sexo == 'M':
        print(f'Sexo: {sexo}')
        corretas = corretas + 1
    else:
        print('Sexo Invalido !')

    if corretas == 5:
        condicao = False
    else:
        corretas = 0
        print('\n')