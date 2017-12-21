from random import randint
rodadas = 0
pontos_jogador = 0
pontos_computador = 0
empates = 0

while True:
    rodadas += 1
    print("Rodada {}.".format(rodadas))
    jogada_usuario = input("Escolha sua jogada entre pedra, papel e tesoura ou saia do jogo: ").lower()
    if jogada_usuario == "pedra" or jogada_usuario == "papel" or jogada_usuario == "tesoura":
        print("Você jogou {}.".format(jogada_usuario))
        jogada_computador = randint(0,3)
        if jogada_computador == 0:
            jogada_computador = "pedra"
        elif jogada_computador == 1:
            jogada_computador = "papel"
        else:
            jogada_computador = "tesoura"
        print("O computador jogou {}.".format(jogada_computador))
        vitoria = False
        empate = False
        if jogada_usuario == "pedra":
            if jogada_computador == "tesoura":
                print("Pedra quebra tesoura. O computador perde.")
                vitoria = True
            elif jogada_computador == "papel":
                print("Papel embrulha pedra. O jogador perde.")
            else:
                print("Nada acontece. O computador também escolheu pedra.")
                empate = True
        elif jogada_usuario == "papel":
            if jogada_computador == "tesoura":
                print("Tesoura corta papel. O computador ganha.")
            elif jogada_computador == "pedra":
                print("Papel embrulha pedra. O jogador ganha.")
                vitoria = True
            else:
                print("Nada acontece. O computador também escolheu papel.")
                empate = True
        elif jogada_usuario == "tesoura":
            if jogada_computador == "pedra":
                print("Pedra quebra tesoura. O computador ganha.")
            elif jogada_computador == "papel":
                print("Tesoura corta papel. O jogador ganha.")
                vitoria = True
            else:
                print("Nada acontece. O computador também escolheu tesoura.")
                empate = True
        if empate:
            print("Rodada terminou em empate.")
            empates += 1
        elif vitoria:
            print("Você venceu a rodada.")
            pontos_jogador += 1
        else:
            print("Você perdeu a rodada.")
            pontos_computador += 1
        print("Rodada {} finalizada.".format(rodadas))
    elif jogada_usuario == "sair":
        break
    else:
        print("Insira uma opção válida.")
        rodadas -= 1

print("Placar do jogo: ")
print("Pontos do jogador:{}.".format(pontos_jogador))
print("Pontos do computador:{}.".format(pontos_computador))
print("Empates:{}".format(empates))

if pontos_jogador > pontos_computador:
    print("Você venceu o jogo.")
elif pontos_jogador < pontos_computador:
    print("Você perdeu o jogo.")
else:
    print("O jogo empatou.")

