"""Dada a lista 'n' com duas listas de números dentro, crie uma função que recebe a lista de
listas como argumento e retorna uma única lista com todos os números encontrados"""


def funcao(lista):
    lista_unica = []
    for sublista in lista:
        for numero in sublista:
            lista_unica.append(numero)
    return lista_unica

n = [[1,2,3], [4,5,6,7,8,9]]
print(funcao(n))



