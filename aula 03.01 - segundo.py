def contar_numeros_pequenos(numeros):
    total = 0

    for numero in numeros:
        if numero < 10:
            total += numero

    return total

# lista = [1, 2, 3, 4] esse é o jeito mais fácil, optei pelo mais difícil

lista = []
for indice in range(3):
    numeros = int(input("Digite um número: "))
    lista.append(numeros)
resultado = contar_numeros_pequenos(lista)
print(resultado)

