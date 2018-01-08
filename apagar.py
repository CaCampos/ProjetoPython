def pegar_inteiro(mensagem):
    numero = ""

    while numero == "":
        try:
            numero = int(input(mensagem))
        except Exception as erro:
            print("Digite um número válido.")
    return numero
