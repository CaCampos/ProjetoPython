numero1_ex1 = int(input("Digite um número inteiro: "))
numero2_ex1 = int(input("Digite outro número inteiro: "))
numero3_ex1 = int(input("Digite outro número inteiro: "))

def pegar_maior_valor(*numeros):
    return max(numeros)
maior_valor = pegar_maior_valor(numero1_ex1, numero2_ex1, numero3_ex1)
print("O maior valor entre os números {}, {} e {} é o {}.".format(numero1_ex1, numero2_ex1, numero3_ex1, maior_valor))

numero1_ex2 = int(input("Digite um número inteiro: "))
numero2_ex2 = int(input("Digite outro número inteiro: "))
numero3_ex2 = int(input("Digite outro número inteiro: "))

def pegar_menor_valor(*numeros):
    return min(numeros)
menor_valor = pegar_menor_valor(numero1_ex2, numero2_ex2, numero3_ex2)
print("O menor valor entre os números {}, {} e {} é o {}.".format(numero1_ex2, numero2_ex2, numero3_ex2,menor_valor))

numero1_ex3 = int(input("Digite um número inteiro positivo: "))
numero2_ex3 = int(input("Digite outro número inteiro positivo: "))
numero3_ex3 = int(input("Digite outro número inteiro positivo: "))

numero4_ex3 = int(input("Digite um número inteiro negativo: "))
numero5_ex3 = int(input("Digite outro número inteiro negativo: "))
numero6_ex3 = int(input("Digite outro número inteiro negativo: "))

modulo_numero4_ex3 = abs(numero4_ex3)
modulo_numero5_ex3 = abs(numero5_ex3)
modulo_numero6_ex3 = abs(numero6_ex3)
print(modulo_numero4_ex3, modulo_numero5_ex3, modulo_numero6_ex3)

def pegar_maior_valor(*numeros):
    return max(numeros)
maior_valor = pegar_maior_valor(numero1_ex3, numero2_ex3, numero3_ex3, numero4_ex3, numero5_ex3, numero6_ex3)
print("O maior valor entre os números {}, {}, {}, {}, {} e {} é o {}.".format(numero1_ex3, numero2_ex3, numero3_ex3,numero4_ex3,numero5_ex3,numero6_ex3, maior_valor))


def pegar_menor_valor(*numeros):
    return min(numeros)
menor_valor = pegar_menor_valor(numero1_ex3, numero2_ex3, numero3_ex3, numero4_ex3, numero5_ex3, numero6_ex3)
print("O menor valor entre os números {}, {}, {}, {}, {} e {} é o {}.".format(numero1_ex3, numero2_ex3, numero3_ex3,numero4_ex3,numero5_ex3,numero6_ex3, menor_valor))

def checar_tipo_variavel(variavel):
	tipo = type(variavel)

	if tipo == int:
		print("Variável formatada: {:05d}".format(variavel))
	elif tipo == float:
		print("Variável formatada: {:.2f}".format(variavel))
	elif tipo == str:
		print("Variável formatada: {:>10}".format(variavel))
	else:
		print("Esse tipo de variável não está mapeado.")
