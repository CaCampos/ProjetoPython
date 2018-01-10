# escrevendo um arquivo

nome_digitado = input("Digite seu nome: ")
idade_digitada = input("Digite sua idade: ")
telefone_digitado = input("Digite seu telefone: ")
data_nascimento_digitada = input("Digite sua data de nascimento: ")
telefone_comercial_digitado = input("Digite seu telefone comercial: ")


arquivo = open("usuario.txt", "w")
arquivo.write("Nome: {}\n".format(nome_digitado))
arquivo.write("Idade: {}\n".format(idade_digitada))
arquivo.write("Telefone: {}\n".format(telefone_digitado))
arquivo.write("Data de nascimento: {}\n".format(data_nascimento_digitada))
arquivo.write("Telefone comercial: {}\n".format(telefone_comercial_digitado))
arquivo.close()
