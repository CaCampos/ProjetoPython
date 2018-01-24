import requests
import json

id_politico = 1
url = "http://politicos.olhoneles.org/api/v0/politicians/{}".format(id_politico)
conteudo_url = requests.get(url)
conteudo_json = json.loads(conteudo_url.text)
print(conteudo_json)

def varrer_lista_dicionarios(lista,chave, exibicao):
    print(exibicao + ":")
    for item in lista:
        print("\t" + item["name"])

def formatar_booleano(variavel):
    if variavel:
        return "Sim"
    else:
        return "Não"

def pegar_valor_dicionario(caminho, base):
    try:
        for item in caminho:
            base = base[item]
    except:
        base = "Valor não informado."
    return base



nomes_alternativos = conteudo_json["alternative_names"]
varrer_lista_dicionarios(nomes_alternativos, "name", "Nomes Alternativos")

cpf = conteudo_json["cpf"]
primeiro_bloco = cpf[0:3]
segundo_bloco = cpf[3:6]
terceiro_bloco = cpf[6:9]
quarto_bloco = cpf[9:11]
print("\tCPF: {}.{}.{}-{}".format(primeiro_bloco, segundo_bloco, terceiro_bloco, quarto_bloco))

etnia = conteudo_json["ethnicity"]["name"]
print("\tEtnia: " + etnia)

data_nascimento = conteudo_json["date_of_birth"]
data_nascimento = data_nascimento.split("-")
data_nascimento.reverse()
data_nascimento = "/".join(data_nascimento)
print("\tData de nascimento: {}".format(data_nascimento))

educacao = conteudo_json["education"]["name"]
print("\tEducação: " + educacao)

genero = conteudo_json["gender"]

estado_civil = conteudo_json["marital_status"]["name"]

if genero == "M":
    print("\tGênero: Masculino")
    estado_civil = estado_civil.replace("(A)", "")
elif genero == "F":
    print("\tGênero: Feminino")
    estado_civil = estado_civil.replace("o(A)", "a")
else:
    print("\tGênero não definido")

print("\tEstado Civil: " + estado_civil)

nacionalidade = conteudo_json["nationality"]["name"]
print("\tNacionalidade: " + nacionalidade)

lugar_nascimento = conteudo_json["place_of_birth"]
print("\tLugar de nascimento: " + lugar_nascimento)

estado_atual = conteudo_json["state"]["name"]
print("\tEstado Atual: " + estado_atual)

ocupacao = conteudo_json["occupation"]["name"]
print("\tOcupação: " + ocupacao)


partidos = conteudo_json["political_parties"]
print()
print("Partidos políticos:")

for partido in partidos:
    nome_partido = partido["political_party"]["name"]
    print("\tNome do Partido: " + nome_partido)
    sigla_partido = partido["political_party"]["siglum"]
    print("\tSigla do Partido: " + sigla_partido)
    numero_tse = partido["political_party"]["tse_number"]
    print("\tNúmero no TSE: {}".format(numero_tse))
    data_inicial = partido["date_start"]
    data_inicial = data_inicial.split("-")
    data_inicial.reverse()
    data_inicial = "/".join(data_inicial)
    print("\tData inicial: {}".format(data_inicial))
    data_final = partido["date_end"]
    if not data_final:
        print("\tA data final não está definida.")
    else:
        data_final = data_final.split("-")
        data_final.reverse()
        data_final = "/".join(data_final)
        print("\tData de final: {}".format(data_final))

print()
candidaturas = conteudo_json["candidacies"]
print("Candidaturas:")
numero = 0

for candidatura in candidaturas:
    numero += 1
    print("{}ª candidatura".format(numero))
    lista_caminho = [
        "city",
        "name"
    ]
    status = candidatura["candidacy_status"]["name"]
    print("\tStatus: " + status)
    eleito = formatar_booleano(candidatura["elected"])
    print("\tEleito: " + eleito)
    cargo = candidatura["political_office"]["name"]
    print("\tCargo: " + cargo)
    estado = pegar_valor_dicionario(["state", "name"], candidatura)
    print("\tEstado: " + estado)

    valor = pegar_valor_dicionario(lista_caminho, candidatura)
    print("\tCidade: {}".format(valor))

