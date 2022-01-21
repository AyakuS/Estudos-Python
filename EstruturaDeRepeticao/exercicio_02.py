'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
'''
condicao = True
while condicao:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    if nome == senha:
        print('Por favor, digite a senha diferente do nome! ')
    else:
        print('Senha cadastrada !')
        condicao = False

