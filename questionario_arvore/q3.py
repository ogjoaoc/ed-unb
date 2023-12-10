class ArvoreBinaria():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def verificaSimetria(raiz):
    def sao_simetricas(raiz1, raiz2):
        if raiz1 is None and raiz2 is None:
            return True
        if raiz1 is None or raiz2 is None:
            return False

        return (raiz1.dado == raiz2.dado and
                sao_simetricas(raiz1.esq, raiz2.dir) and
                sao_simetricas(raiz1.dir, raiz2.esq))

    if raiz is None:
        return True
    
    return sao_simetricas(raiz.esq, raiz.dir)


raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))  # Saída: True
