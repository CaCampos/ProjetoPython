checar_numero = int(input("Escreva um número para saber se ele é primo: "))
contador = 0
for numero in range(checar_numero):
    if checar_numero % (numero + 1) == 0:
        contador += 1
if contador == 2:
    print("O número {} é primo.".format(checar_numero))
else:
    print("O número {} não é primo.".format(checar_numero))



