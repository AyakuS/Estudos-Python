"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

turma = int(input('Digite a quantidade de turmas disponiveis: '))
count = 0
total_alunos = 0
if turma == 0:
    print('valor é invalido! ')
else:
    while count < turma:
        count += 1
        qtd_alunos = int(input(f'Turma {count}: '))
        total_alunos += qtd_alunos

media_alunos = total_alunos/turma

if media_alunos > 40:
    print(f'A média é de 40 alunos por sala, média atual {media_alunos}')

else:
    print(f'Média de alunos por sala é de {media_alunos}')

