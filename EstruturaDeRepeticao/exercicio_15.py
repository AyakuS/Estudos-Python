'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
até o n−ésimo termo
'''

n = int(input('Que termo deseja encontrar: '))
primeiro = 1
segundo = 1
termo = 0

if (n==1) or (n==2):
    print(1)
else:
   count = 3

    while count <= n:

        termo = primeiro + segundo
        segundo = primeiro
        primeiro = termo
        count += 1
    print(f'O N-ésimo termo é: {termo}')
