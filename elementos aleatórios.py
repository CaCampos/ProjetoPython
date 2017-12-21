"""exemplo"""
from random import randint

lista = [5,10,15,20,25]

indice_aleatorio = randint(0,len(lista) - 1)
elemento_aleatorio = lista[indice_aleatorio]
print(elemento_aleatorio)

"""exercício"""
from random import randint

lista = []
for n in range(3):
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)
print(lista)

indice_aleatorio = randint(0,len(lista) -1)
elemento_aleatorio = lista[indice_aleatorio]
print(elemento_aleatorio.upper())

"""Exercício 2"""

nome_completo = "Camila Campos Cabral"
indice_aleatorio = randint(0,len(nome_completo) -1)
elemento_aleatorio = nome_completo[indice_aleatorio]
print(elemento_aleatorio)
