"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

"""
lista_temperaturas = [88,28,35,37,38,21,19,5,8,28,35,45,55]
count = 0

while count < len(lista_temperaturas):
    aux = lista_temperaturas[count+1]
    if lista_temperaturas[count] > aux:
        maior = lista_temperaturas[count]
        
    count+=1

