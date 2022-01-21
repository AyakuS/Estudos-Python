'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

qtd_pessoas = input('Digite a quantidade de pessoas no grupo: ')
qtd_pessoas = int(qtd_pessoas)
lista_pessoas_idade = {}
idade_soma = 0

for n in range(1,qtd_pessoas+1):
    nome = input('Nome do membro: ')
    idade = int(input('Idade do membro: '))
    lista_pessoas_idade[nome] = idade

for n in lista_pessoas_idade:
    idade_soma += lista_pessoas_idade.get(n)
media = idade_soma/len(lista_pessoas_idade)

if media >= 0 and media <= 25:
    print('Turma é jovem !')
elif media >= 26 and media <= 60:
    print('Turma é Adulta !')
else:
    print('Turma é Idosa!')

