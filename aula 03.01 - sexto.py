inventario = {
    "dinheiro": 500,
    "carteira": ["joia", "cartao", "caderno"],
    "mochila": ["faca", "blusa", "guarda-chuva", "garrafa"]
}
print(inventario)

"""adicione R$ 50,00 ao elemento 'dinheiro' do inventário"""

inventario["dinheiro"] = inventario["dinheiro"] + 50
print(inventario["dinheiro"])

"""Adicione um novo item à carteira"""

inventario["carteira"].append("comida")
print(inventario["carteira"])

"""Ordene os itens da bolsa por ordem alfabética"""
inventario["mochila"].sort()
print(inventario["mochila"])

"""Exiba na tela quantos itens a pessoa tem na carteira e na mochila"""
len(inventario["carteira"])
print(len(inventario["carteira"]))

len(inventario["mochila"])
print(len(inventario["mochila"]))

"""Adicione uma nova lista ao inventário chamada 'bolso' e inclua alguns itens"""

inventario["bolso"] = ["chave", "bala", "celular"]
print(inventario)



