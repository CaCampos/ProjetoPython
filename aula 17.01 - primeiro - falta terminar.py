presidenciaveis = [
    {
        "nome_completo": "Luís Inácio Lula da Silva",
        "partido":"PT",
        "número": "13",
        "cargo":"Presidente",
        "votos": 0
    },

    {
        "nome_completo": "Geraldo Alckmin",
        "partido": "PSDB",
        "número": "45",
        "cargo": "Presidente",
        "votos": 0
    },

    {
        "nome_completo": "Jair Bolsonaro",
        "partido": "PSC",
        "número": "20",
        "cargo": "Presidente",
        "votos": 0
    },

    {
        "nome_completo": "Luciano Huck",
        "partido": "PPS",
        "número": "23",
        "cargo": "Presidente",
        "votos": 0
    },

    {
       "nome_completo": "Marina Silva",
        "partido": "REDE Sustentabilidade",
        "número": "18",
        "cargo": "Presidente",
        "votos": 0
    },

    {
        "nome_completo": "Ciro Gomes",
        "partido": "PDT",
        "número": "12",
        "cargo": "Presidente",
        "votos": 0
    }
]

votos_validos = 0
votos_brancos = 0
votos_nulos = 0

while True:
    voto = (input("Informe seu voto para a presidência do Brasil (2 dígitos) ou digite a palavra branco para votar em branco ou digite encerrar votação para fechar: "))

    if voto == "encerrar votação":
        print("Você optou por encerrar a votação.")
        break
    if voto == "branco":
        print("Seu voto é branco.")
        votos_brancos += 1
    politico_votado = None
    for presidenciavel in presidenciaveis:
        if voto == presidenciavel["número"]:
            nome_completo = presidenciavel["nome_completo"]
            partido = presidenciavel["partido"]
            politico_votado = presidenciavel
            politico_votado["votos"] += 1
            print("Seu voto vai para {}. Ele é do partido {}.".format(nome_completo, partido))
            votos_validos += 1
    if not politico_votado:
        print("Esse não é um candidato válido. Seu voto é nulo.")
        votos_nulos += 1
    acao = input("Digite confirmar, corrigir ou cancelar: ")
    if acao == "corrigir" or acao == "cancelar":
        print("Você optou por corrigir ou cancelar seu voto. Vote novamente.")
    elif acao == "confirmar":
        print("Voto computado.")


def pegar_total_votos():
    votos_total = 0
    for presidenciavel in presidenciaveis:
        votos_total += presidenciavel["votos"]
    return votos_total


print()
def pegar_porcentagem():
    votos_total = pegar_total_votos()
    for presidenciavel in presidenciaveis:
        porcentagem_presidenciavel = (presidenciavel["votos"] * 100) / votos_total
        print()
        print("O político {} recebeu {}% dos votos válidos.".format(presidenciavel["nome_completo"], porcentagem_presidenciavel))


print()
print("Votos válidos: {}.".format(votos_validos))
print("Votos brancos: {}.".format(votos_brancos))
print("Votos nulos: {}.".format(votos_nulos))


for presidenciavel in presidenciaveis:
    if presidenciavel["votos"] == 1:
        print("O político {} recebeu {} voto.".format(presidenciavel["nome_completo"],presidenciavel["votos"]))
    elif presidenciavel["votos"] > 1:
            print("O político {} recebeu {} votos.".format(presidenciavel["nome_completo"],presidenciavel["votos"]))

def exibir_politico(presidenciavel):
    porcentagem = pegar_porcentagem(presidenciavel)
    plural = "" if presidenciavel["votos"] == 1 else "s"
    print("Político '{}' do partido '{}' recebeu '{}' voto{} e ficou com '{:.2f}%' dos votos válidos.".format(presidenciavel["nome"], presidenciavel["partido"], presidenciavel["votos"], plural, porcentagem))

def exibir_resultado_eleicao():

    primeiro_lugar = None
    segundo_lugar = None

    for presidenciavel in presidenciaveis:
        if not primeiro_lugar or presidenciavel["votos"] > primeiro_lugar["votos"]:
            segundo_lugar = primeiro_lugar

            primeiro_lugar = presidenciavel
        elif not segundo_lugar or presidenciavel["votos"] > segundo_lugar["votos"]:
            segundo_lugar = presidenciavel

    porcentagem = pegar_porcentagem(primeiro_lugar)

    if porcentagem > 50:
        print("O vencedor da eleição é o político '{}' com '{:.2f}%' dos votos válidos.".format(primeiro_lugar, porcentagem))
    else:
        print("A votação encerrou em segundo turno.")
        print("Os políticos que irão para o segundo turno são:")
        exibir_politico(primeiro_lugar)
        exibir_politico(segundo_lugar)

exibir_resultado_eleicao()

def exibir_politicos():
    print("Resultado geral da votação:")
    for presidenciavel in presidenciaveis:
        exibir_politico(presidenciavel)
exibir_politicos()
