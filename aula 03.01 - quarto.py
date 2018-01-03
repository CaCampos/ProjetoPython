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
            "Social democracia"
        ]
    }
}

ideologia_pt = partidos["PT"]["ideologias"]
for ideologia in ideologia_pt:
    print(ideologia)
print(ideologia_pt)

def contar_ideologias(partido):
    return len(partidos[partido]["ideologias"])

sigla_partido = "PV"

quantidade_ideologias = contar_ideologias(sigla_partido)
print("O partido {} possui {} ideologias.".format(sigla_partido, quantidade_ideologias))




