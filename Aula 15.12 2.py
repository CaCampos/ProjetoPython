lista_nomes = []
for indice in range(3):
    nome = input("Digite o {}º nome: ".format(indice + 1))
    lista_nomes.append(nome)
print(lista_nomes)

lista_nomes.sort()
print(lista_nomes)



