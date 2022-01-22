"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

"""
lista_temperaturas = [28,35,37,38,21,19,5,8,28,35,45,55]
maior, menor = None, None
media = 0

for n in range(len(lista_temperaturas)):
    media += lista_temperaturas[n]
    if n == 0:
        maior = menor = lista_temperaturas[n]
    else:
        if lista_temperaturas[n] > maior:
            maior = lista_temperaturas[n]
        if lista_temperaturas[n] < menor:
            menor = lista_temperaturas[n]


print(f"Maior Temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Média dos dias: {media/len(lista_temperaturas)}°C")
