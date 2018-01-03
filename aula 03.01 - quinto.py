partidos = {
    "PT": {
        "nome": "Partido dos Trabalhadores",
        "sede": "Brasília",
        "presidente": "Gleisi Hoffman",
        "numero_eleitoral": 13,
        "candidato_proprio": True,
        "ideologias": [
            "Socialismo democrático",
            "Desenvolvimentismo",
            "Lulismo",
            "Trotskismo",
            "Democracia"
        ]
    },
    "PV": {
        "nome": "Partido Verde",
        "sede": "São Paulo",
        "presidente": "José Luiz Penna",
        "numero_eleitoral": 43,
        "candidato_proprio": False,
        "ideologias": [
            "Ambientalismo",
            "Ecologismo",
            "Liberalismo social",
            "Progressismo",
            "Social democracia",
            "Democracia"
        ]
    }
}


"""Varrer o dicionário de partidos, pegar as ideologias de cada partido, checar se a
ideologia em questão está dentro da lista de ideologias do partido. se estiver, armazenar
a sigla do partido em uma lista nova, retornar a lista nova. 

Dicas: criar uma nova lista, usar o método "count" para saber se a ideologia está na lista
do partido ou não, usar o "append" para adicionar a sigla do partido na lista nova"""

def procurar_partidos_ideologia(ideologia):
    lista_partidos = []
    for partido in partidos:
        ideologias = partidos[partido]["ideologias"]
        checagem_ideologias = ideologias.count(ideologia)
        if checagem_ideologias > 0:
            lista_partidos.append(partido)
    return lista_partidos
partidos_democracia = procurar_partidos_ideologia("Democracia")
print(partidos_democracia)

def procurar_partidos_ideologia(ideologia):
    lista_partidos = []
    for partido in partidos:
        ideologias = partidos[partido]["ideologias"]
        checagem_ideologias = ideologias.count(ideologia)
        if checagem_ideologias > 0:
            lista_partidos.append(partido)
    return lista_partidos
partidos_socialismo_democratico = procurar_partidos_ideologia("Socialismo democrático")
print(partidos_socialismo_democratico)

