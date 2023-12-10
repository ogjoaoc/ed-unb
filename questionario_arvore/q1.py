class NoArvoreBB():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def insere(raiz, no):
    if not raiz:
        return no
    
    if no.dado < raiz.dado:
        raiz.esq = insere(raiz.esq, no)
    else:
        raiz.dir = insere(raiz.dir, no)

    return raiz


def preorder(raiz):
    if raiz:
        print(raiz.dado, end=" ")
        preorder(raiz.esq)
        preorder(raiz.dir)

def inorder(raiz):
    if raiz:
        inorder(raiz.esq)
        print(raiz.dado, end=" ")
        inorder(raiz.dir)

def posorder(raiz):
    if raiz:
        posorder(raiz.esq)
        posorder(raiz.dir)
        print(raiz.dado, end=" ")

primeiro = False
raiz = None
while (True):
    n = input()
    if n == "quack":
        break
    elif n.isdigit():
        if not primeiro:
            raiz = NoArvoreBB(int(n))
            primeiro = True
        else:
            raiz = insere(raiz, NoArvoreBB(int(n)))
    elif n == "in":
        if raiz != None:
            inorder(raiz)
            print(" ")
        else:
            print(" ")
    elif n == "pre":
        if raiz != None:
            preorder(raiz)
            print(" ")
        else:
            print("")
    elif n == "pos":
        if raiz != None:
            posorder(raiz)
            print(" ")
        else:
            print(" ")