def exibir_lista(lista, exibir_chave=False):
    for chave in range(len(lista)):
        valor = lista[chave]
        if exibir_chave:
            print("{}: {}".format(chave, valor))
        else:
            print("{}".format(valor))


numeros = [10, 5, 6, 7, 9, 10]
exibir_lista(numeros, True)
"""se colocar false só aparecem os valores"""
