"""primeiro exemplo"""
def checar_ocorrencias_letra_em_texto(texto, checar_letra):
    numero_ocorrencias = 0
    for indice in range(len(texto)):
        letra = texto[indice]
        if checar_letra == letra:
            numero_ocorrencias = numero_ocorrencias + 1
    return numero_ocorrencias

texto_usuario = input("Digite um texto: ")
letra_usuario = input("Digite uma letra: ")
ocorrencias = checar_ocorrencias_letra_em_texto(texto_usuario, letra_usuario)
print("A letra '{}' está presente {} vezes no texto '{}'.".format(letra_usuario, ocorrencias, texto_usuario))

"""segundo exemplo"""
def contar_numeros_pequenos(numeros):
    total = 0
    for numero in numeros:
        if numero < 10:
           total = total + numero
    return total
lista = [1,2,3, 20, 50, 100, 150, 200]
total_soma = contar_numeros_pequenos(lista)
print(total_soma)

def somar(numero1, numero2, numero3, numero4):
    print("somar")
    print(numero1)
    print(numero2)
    print(numero3)
    print(numero4)
    total = numero1 + numero2 + numero3 + numero4
    print(total)
    return total

resultado = somar(1,2,3,4)
print(resultado * 12)

"""exemplo com args"""
def somar(*numeros):
    print("somar")
    print(numeros)
    total = sum(numeros)
    print(total)
    return total
resultado = somar (1,2,3,4,5,6,7,8,9,10)
print(resultado * 600)

"""exemplo com listas"""

def criar_lista(quantidade_numeros):
    print("criar lista")
    lista = []
    for numero in range (quantidade_numeros):
        numero_digitado = int(input("Digite o {}º número: "))
    

