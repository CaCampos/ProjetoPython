def custo_hotel(noites):
    return noites * 140
resultado = custo_hotel(3)
print(resultado)

def custo_aviao(cidade):
    print(cidade)
    if cidade == "SP":
        return 312.0
    elif cidade == "POA":
        return 447.0
    elif cidade == "Recife":
        return 831.0
    elif cidade == "Manaus":
        return 986.0
    else:
        print("Destino não disponível.")

passagem = custo_aviao("Manaus")
print(passagem)

def custo_carro(dias):
    custo = 40 * dias

    if dias >= 7:
        return custo - 50
    elif dias >= 3:
        return custo - 20
    return custo

custo = custo_carro(3)
print(custo)

def custo_viagem(cidade,dias,reais):
    return custo_hotel(dias) + custo_aviao(cidade) + custo_carro(dias) + gastos_extras(reais)

custo = custo_viagem("Manaus",12,gastosextras(800))
print(custo)





















