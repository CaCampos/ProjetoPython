Paulo = {
    "nome":"Paulo Salvatore",
    "atividades": [10.0, 8.0, 7.5],
    "quizzes": [8.5, 9.0, 6.5],
    "testes": [5.0, 9.5]
}

Luisa = {
    "nome":"Luísa Oliveira",
    "atividades": [7.0, 6.0, 9.5],
    "quizzes": [6.0, 8.0, 7.0],
    "testes": [4.5, 8.5]
}

Ana = {
    "nome":"Ana Lúcia",
    "atividades": [2.0, 7.0, 3.5],
    "quizzes": [2.5, 1.0, 3.0],
    "testes": [3.0, 4.0]
}

estudantes = [Paulo, Luisa, Ana]

def media(numeros):
    total = sum(numeros)
    return total / len(numeros)

def pegar_media(aluno):
    media_atividades = media(aluno["atividades"])
    media_quizzes = media(aluno["quizzes"])
    media_testes = media(aluno["testes"])

    total = (media_atividades * 0.1) + (media_quizzes * 0.3) + (media_testes * 0.6)

    return total

def checar_aprovacao(aluno):
    nome = aluno["nome"]
    media_calculada = pegar_media(aluno)
    print("Aluno: {}\nMédia: {:.2f}".format(nome, media_calculada))
    if media_calculada < 4.0:
        print("\t{} foi reprovado.".format(nome))
    elif media_calculada < 6.0:
        print("\t{} está de exame.".format(nome))
    else:
        print("\t{} foi aprovado.".format(nome))
    print()

def pegar_media_classe(alunos_classe):
    medias_alunos_classe = []

    for aluno_classe in alunos_classe:
        media_calculada = pegar_media(aluno_classe)
        medias_alunos_classe.append(media_calculada)

    media_classe = media(medias_alunos_classe)

    return media_classe

for estudante in estudantes:
    checar_aprovacao(estudante)

media_classe_calculada = pegar_media_classe(estudantes)
print("Média da Classe: {:.2f}".format(media_classe_calculada))


"""for estudante in estudantes:
print(nome)
print(atividades)
print(media(atividades))
print(quizzes)
print(testes)
print()"""

