import json
import requests

# Pegar palavra digitada pelo usuário
# Inserir palavra na base_url, no lugar de {query}
# Pegar o conteúdo dessa URL utilizando o requests
# Transformar o conteúdo em JSON
# Exibir na tela a quantidade de piadas encontradas

palavra_busca = input("Digite uma palavra a ser encontrada em nosso arquivo de piadas: ")
base_url = "https://api.chucknorris.io/jokes/search?query={}".format(palavra_busca)
conteudo = requests.get(base_url)
conteudo = json.loads(conteudo.text)
print("O total de piadas encontradas com a palavra {} foi: {}".format(palavra_busca, conteudo["total"]))

piadas = conteudo["result"]


# Criar funções:
# exibir_piadas(piadas)
# exibir_piada_pelo_indice(piadas,indice)
# exibir_piada(piada)

def exibir_piada(piada, campo="value"):
    print(piada[campo])

def exibir_piada_pelo_indice(lista_piadas, indice):
    exibir_piada(lista_piadas[indice])

def exibir_piadas(lista_piadas):
    for indice, piada in enumerate(lista_piadas):
        exibir_piada_pelo_indice(lista_piadas, indice)

exibir_piadas(piadas)


