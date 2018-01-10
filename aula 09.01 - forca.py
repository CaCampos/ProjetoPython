"""
Exercício 26

Nome: Jogo da Forca
Objetivo: Desenvolver um jogo da forca completo.
Dificuldade: Intermediário

1 - O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
2 - O jogador poderá errar 6 vezes antes de ser enforcado.
3 - No começo do jogo exiba quantas letras tem a palavra.
4 - O jogo deverá ser exibido na seguinte estrutura:
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""
print("Jogo da Forca")
from random import randint
lista_de_palavras = ["deadlift", "cleanandjerk", "squatclean", "medball", "wallball", "abmat", "pullup", "pushup", "frontsquat", "backsquat"]
indice_aleatorio = randint(0,len(lista_de_palavras) - 1)
elemento_aleatorio = lista_de_palavras[indice_aleatorio]
print("A palavra tem {} letras.".format(len(elemento_aleatorio)))

def pegar_letra_digitada():
    return input("Digite uma letra: ")

lista_auxiliar = []
erros = 0
acertos = 0

while True:
    letra_digitada = pegar_letra_digitada()

    if elemento_aleatorio.count(letra_digitada) > 0:
        print("A letra {} está presente na palavra.".format(letra_digitada))
        acertos += elemento_aleatorio.count(letra_digitada)
    else:
        erros += 1
        print("Você errou pela {}ª vez! Tente de novo.".format(erros))

    if erros == 6:
        print("Você excedeu o limite de erros.")
        break


    palavra = ""


    lista_auxiliar.append(letra_digitada)


    for letra in elemento_aleatorio:
        if lista_auxiliar.count(letra) >= 1:
            palavra += letra
        else:
            palavra += "_"
        palavra += " "
    print("A palavra é: {}.".format(palavra))

    if acertos == len(elemento_aleatorio):
        break
