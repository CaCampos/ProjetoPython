lista_pessoas = []


def procurar_pessoa():
    nome = input("Escreva o nome da pessoa que deseja remover ou editar: ")
    for pessoa in lista_pessoas:
        if pessoa["Nome"] == nome:
            return pessoa

    print("A pessoa não foi encontrada.")
    print("Tente novamente.")

while True:

    resposta_usuario = input("Qual ação você deseja realizar? \n Digite 'C' ou 'Cadastrar' p/ cadastrar uma nova pessoa \n 'L' ou 'Listas' para listar as pessoas cadastradas \n 'R' ou 'Remover' para remover uma pessoa \n 'E' ou 'Editar' para editar uma pessoa previamente cadastrada. \n Caso queira sair, digite cancelar: ").lower()
    if resposta_usuario == "c" or resposta_usuario == "cadastrar":
        pessoas = {}
        pessoas["Nome"] = input("Qual é o nome da pessoa? ")
        pessoas["Sobrenome"] = input("Qual é o sobrenome da pessoa? ")
        pessoas["Telefone"] = input("Qual é o telefone da pessoa? ")
        pessoas["CPF"] = input("Qual é o CPF da pessoa? ")
        lista_pessoas.append(pessoas)
        print(lista_pessoas)
        print("Você conseguiu cadastrar o contato com sucesso.")
    elif resposta_usuario == "r" or resposta_usuario == "remover":
        pessoa = procurar_pessoa()
        indice_pessoa = lista_pessoas.index(pessoa)
        print(lista_pessoas)
        del lista_pessoas[indice_pessoa]
        print(lista_pessoas)
        print("Você conseguiu remover o contato com sucesso.")
    elif resposta_usuario == "e" or resposta_usuario == "editar":
        pessoa = procurar_pessoa()
        indice_pessoa = lista_pessoas.index(pessoa)
        nova_pessoa = {
            "Nome": input("Nome: "),
            "Sobrenome": input("Sobrenome: "),
            "Telefone": input("Telefone: "),
            "CPF": input("CPF: ")

        }
        lista_pessoas[indice_pessoa] = nova_pessoa
        print("Você conseguiu editar o contato com sucesso")
    elif resposta_usuario == "l" or resposta_usuario == "listar":
        print(lista_pessoas)
        print("Você conseguiu listar as pessoas cadastradas com sucesso.")
    elif resposta_usuario == "cancelar":
        print("Você saiu.")
        break


