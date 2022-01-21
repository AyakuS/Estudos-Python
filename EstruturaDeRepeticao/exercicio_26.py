'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
'''
import os

candidatos = {13:'Gabriel Hangrad',
              45:'Felipe Barbosa',
              24:'Alex Matos', }

print('Candidatos para Votação!')
print(candidatos)

qtd_eleitores = int(input('Digite a quantidade de Eleitores: '))
votos_computados = {}
contador_votos = 0

def valida_voto(voto):

    if votos_computados.get(voto):
        aux = votos_computados[voto][0]
        aux = aux + 1
        votos_computados[voto] = [aux]
    else:
        votos_computados[voto] = [conta_voto + 1]


while contador_votos < qtd_eleitores:
   voto = int(input('\nDigite seu voto: '))
   conta_voto = 0
   if candidatos.get(voto):

       if voto == 13:
           valida_voto(voto)
           print('\nVoto validado !')


       elif voto == 45:
           valida_voto(voto)
           print('\nVoto validado !')


       elif voto == 24:
           valida_voto(voto)
           print('\nVoto validado !')


   else:

       if votos_computados.get('Anulados'):
           aux = votos_computados['Anulados'] = 0
           aux = aux + 1
           votos_computados['Anulados'] = [aux]
           print('\nVoto Anulado\n')


       else:
           votos_computados['Anulados'] = [conta_voto + 1]
           print('\nVoto Anulado\n')


   contador_votos += 1

for i in sorted(votos_computados, key=votos_computados.get, reverse=True):
    print(f'{i} - {candidatos.get(i)}: Votos{votos_computados[i]}')