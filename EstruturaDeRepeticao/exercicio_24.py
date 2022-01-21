'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
notas = []
qtd_notas = input('Digite a quantida de notas: ')
qtd_notas = int(qtd_notas)
soma = 0
for n in range(1,qtd_notas+1):
    notas.append(int(input(f'Digite a Nota {n}: ')))

for n in notas:
    soma += n
print(f'Media: {soma / qtd_notas}')
