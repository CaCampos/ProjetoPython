"""item 1"""
lista = [1,2,3,4,2,3,5,7,5,7,8,1,3,2,15,18,20,25,33,1]
lista.sort()
print(lista)
"""item 2"""
len(lista)
print(len(lista))
"""item 3"""
nova_lista = []
for numero in lista:
    if lista.count(numero) > 1 and nova_lista.count(numero) == 0:
        print("O número {} está repetido.".format(numero))
        nova_lista.append(numero)
print(nova_lista)

"""item 4"""
from random import randint
lista_aleatoria = []
for numero in range(20):
    lista_aleatoria.append(randint(1,30))
print(lista_aleatoria)

"""item 5"""
def detectar_numeros_repetidos(lista):
    nova_lista = []
    for numero in lista:
        if lista.count(numero) > 1 and nova_lista.count(numero) == 0:
            nova_lista.append(numero)
lista = [1,2,3,4,2,3,5,7,5,7,8,1,3,2,15,18,20,25,33,1]
print(nova_lista)

"""item 6"""
def detectar_numeros_repetidos(lista_aleatoria):
    nova_lista = []
    for numero in lista_aleatoria:
        if lista_aleatoria.count(numero) > 1 and nova_lista.count(numero) == 0:
            nova_lista.append(numero)
    return nova_lista
teste = detectar_numeros_repetidos(lista_aleatoria)
print(lista_aleatoria)
print(teste)

"""item 7"""
def 
