""""Dicionários"""

pessoas = {
    "SP": 447,
    "RJ": 323,
    "MG": 121
}
print(pessoas)
print(pessoas["SP"])
print(pessoas.get("SP"))
"""se o elemento do get não existir, aparece none no print"""

refeicoes = {
    "Café da manhã": 0,
    "Almoço": 40,
    "Café da tarde": 20,
    "Jantar": 30
}

refeicoes["Trufa"] = 5.51
"""Adicionando elemento na biblioteca"""
print(refeicoes)
print(refeicoes["Almoço"])
for refeicao in refeicoes:
    preco = refeicoes[refeicao]
    print(refeicao)
    print(preco)
    print()
preco_jantar = refeicoes.get("Jantar")
print(preco_jantar)

def pegarRefeicao(indice):
    refeicao = refeicoes.get(indice)
    if refeicao == None:
        print("Refeição não existe")
    else:
        print("Refeição: {}".format(refeicao))
    return refeicao
custo1 = pegarRefeicao("Almoço")
custo2 = pegarRefeicao("Jantar")
conta = 0
conta = conta + custo1
conta = conta + custo2
print(conta)

"""del refeicoes["Jantar"]
print(refeicoes)"""

"""lista = ["Camila", "Campos"]
print(lista)
lista.remove("Camila")
print(lista)"""

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

"""total = 0
for fruta in precos:
    preco = precos[fruta]
    estoque = estoques[fruta]
    print("Fruta {}".format(fruta))
    print("\tPreço {}".format(preco))
    print("\tEstoque {}".format(estoque))
    total += preco * estoque
print("Total das frutas: R$ {}".format(total))"""


def computar_compra(mantimento):
    total = 0
    for fruta in mantimento:
        preco = precos[fruta]
        estoque = estoques[fruta]
        if estoque > 0:
            total += preco
    print("Total das frutas: R$ {}".format(total))

computar_compra(mantimentos)







