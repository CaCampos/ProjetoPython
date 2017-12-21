precos = {
    "Banana": 4,
    "Maçã": 2,
    "Laranja": 1.5,
    "Pera": 3
}

estoques = {
    "Banana": 6,
    "Maçã": 0,
    "Laranja": 32,
    "Pera": 15
}

mantimentos = [
    "Banana",
    "Laranja",
    "Maçã"
]

def computar_compra(mantimento):
    total = 0
    for fruta in mantimento:
        preco = precos[fruta]
        total += preco
    print("Total das frutas: R$ {:.2f}".format(total))
    return total

computar_compra(mantimentos)
