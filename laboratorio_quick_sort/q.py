def quickSort(alist):
    if len(alist) <=1:
        return alist
    esquerda, pivo, direita = reordena(alist)
    esquerda = quickSort(esquerda)
    direita = quickSort(direita)
    esquerda.append(pivo)
    esquerda.extend(direita)
    return esquerda

def reordena(alist):
    pivo = alist[0]
    esquerda = []
    direita = []
    i = 1
    while i < len(alist):
        if alist[i] > pivo:
            direita.append(alist[i])
        else:
            esquerda.append(alist[i])
        i += 1
    return esquerda, pivo, direita
