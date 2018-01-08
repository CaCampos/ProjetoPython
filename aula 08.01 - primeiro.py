"""função items"""

dicionario = {
    1:2,
    3:4
}

for indice in dicionario:
    valor = dicionario[indice]
    print(indice, valor)

for indice, valor in dicionario.items():
    print(indice,valor)
    """mesma coisa de cima, é pra facilitar"""


"""função enumerate - primeiro exemplo"""

lista = [1,2,3]

for indice, valor in enumerate(lista):
    print(indice, valor)

"""função enumarate - segundo exemplo"""

animais = ["gato", "cachorro", "papagaio"]

for indice, animal in enumerate(animais):
    print(indice, animal)

"""função args com argumento opcional"""

def somar_tudo(*numeros, exibir=False):

    total = sum(numeros)
    if exibir:
        print(total)
    return total


resultado = somar_tudo(1, 2, 3, 4, 5, 6, 7, exibir=True)

