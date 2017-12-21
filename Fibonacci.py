numero_usuario = int(input("Digite a quantidade de elementos que deseja ter na sua Sequência de Fibonacci: "))
lista = [1, 1]
for numero in range(numero_usuario - 2):
    primeiro_elemento = lista[numero]
    print(primeiro_elemento)
    segundo_elemento = lista[numero + 1]
    print(segundo_elemento)
    novo_elemento = primeiro_elemento + segundo_elemento
    lista.append(novo_elemento)
    print()

print(lista)



