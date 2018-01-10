# primeiro exemplo
"""from random import randint"""

matriz = []

for i in range(5):
    lista = ["O" * 5]
    matriz.append(lista)

print(matriz)


# segundo exemplo
palavra = "Paulo Salvatore"   #*****
palavra_escondida = "*" * len(palavra)
print(palavra, palavra_escondida)

# terceiro exemplo

palavra = "Paulo Salvatore"
palavra_quebrada = palavra.split(" ")
esconder = "Paulo"

for indice, valor in enumerate(palavra_quebrada):
    if valor == esconder:
        palavra_quebrada[indice] = "*" * len(valor)
palavra_agrupada = " ".join(palavra_quebrada)
print(palavra_agrupada)

