'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''
tamanho_arq = float(input('Digite o tamanho do arquivo: '))
velocidade_link = float(input('Digite a velocidade do seu link: '))
velocidade_download = velocidade_link*8
tempo_donwload = tamanho_arq*velocidade_download
print('O tempo do seu downlaod será de {} minutos'.format(tempo_donwload/60))

