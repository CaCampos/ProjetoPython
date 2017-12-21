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
    print("Sua compra foi realizada com sucesso.")
    total = 0
    for fruta in mantimento:
        preco = precos[fruta]
        estoque = estoques[fruta]
        if estoque > 0:
            print("Você comprou a fruta {}.".format(fruta))
            print("\tVocê pagou {} pela fruta.".format(preco, fruta))
            total += preco
            estoques[fruta] = estoques[fruta] - 1
    print("Total das frutas: R$ {}".format(total))
"""print(estoques)"""
computar_compra(mantimentos)
"""print(estoques)"""

