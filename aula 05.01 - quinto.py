def funcao(argumento1, argumento2=0):
    print("Argumento1: {}".format(argumento1))
    print("Argumento2: {}".format(argumento2))
funcao(10,20)


def somar(a,b, exibir=False):
    total = a + b

    if exibir: """== True"""
    print(total)

    return total

numero1 = 10
numero2 = 20
resultado = somar(numero1,numero2, True)

def exibir(lista,exibir_chaves=False):
    for item in lista:
        if exibir_chaves:
            print("Chave: {}, Valor: {}.".format(lista.index(item), item))
        else:
            print("Valor: {}.".format(item))

lista = [1,2,3,4,5]
exibir(lista,True)

