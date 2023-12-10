def divisores(inteiro):
    divisores_lista = []
    for i in range(1, inteiro + 1):
        if inteiro % i == 0:
            divisores_lista.append(i)
    return divisores_lista
    