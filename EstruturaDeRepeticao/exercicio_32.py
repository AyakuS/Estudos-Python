"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""
#fatorial = n*(n-1)

fatorial = int(input("Qual numero deseja saber o fatorial: "))

if fatorial < 0:
    print("Não existe fatorial negativo ! ")

elif fatorial == 0 or fatorial == 1:
    print(f'O Fatorial de {fatorial} é 1')

else:
    result = 1
    fat = fatorial
    resp = ""
    while fat >= 1:

        result *= fat

        if resp == "":
            resp = str(fat)
        else:
            nova_string = "." + str(fat)
            resp = resp + nova_string

        fat -= 1

    print(f"{fatorial}! = {resp} = {result}")

