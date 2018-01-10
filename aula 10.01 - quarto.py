# lendo um arquivo

arquivo = open("usuario.txt", "r")
conteudo_arquivo = arquivo.read()
print(conteudo_arquivo)
linhas = conteudo_arquivo.split("\n")

usuario = {}

def tratar_chave(chave):
    chave = chave.lower()
    chave = chave.replace(" de ", " ")
    chave = chave.replace(" ", "_")
    return chave

def checar_inteiro(valor):
    try:
        valor = int(valor)
    except:
        pass

    return valor


def tratar_valor(valor):
    valor = checar_inteiro(valor)
    return valor

for linha in linhas:
    informacao_quebrada = linha.split(": ")

    try:
        chave = tratar_chave(informacao_quebrada[0])
        valor = tratar_valor (informacao_quebrada[1])
        usuario[chave] = valor
    except:
        pass

print(usuario)
arquivo.close()


"""linha = arquivo.readline()
while linha:
    print(linha)
    linha = arquivo.readline()"""
