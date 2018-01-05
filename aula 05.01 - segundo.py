"""Crie uma função que receba uma lista de números qualquer e retorne todos os elementos
 dessa lista multiplicados por 2"""

def multiplicar(lista_numeros):
    lista_multiplicados = []
    for numero in lista_numeros:
        lista_multiplicados.append(numero * 2)
    return lista_multiplicados

lista_numeros = [3,4,7,9]
print(multiplicar(lista_numeros))

"""Crie uma função que receba uma lista qualquer e exiba todos os elementos dessa lista
na tela"""

def exiba(lista):
    for numero in lista:
        print(numero)

lista = [1,5,9,0]
exiba(lista)

"""Declare uma lista qualquer, passe-a pela função criada no item 2 e exiba-a utilizando
a função criada no item 3"""

lista_normal = [5,9,0,4]
lista_multiplicada = multiplicar(lista_normal)
exiba(lista_multiplicada)

