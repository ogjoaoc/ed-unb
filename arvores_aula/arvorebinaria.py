class Queue():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
        

class NoArvoreBB():
    def __init__(self, dado, esq=None, dir =None):
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
    print(raiz.dado, end=" ")
    if raiz.esq:
        preorder(raiz.esq)
    if raiz.dir:
        preorder(raiz.dir)

def inorder(raiz):
    if raiz.esq:
        inorder(raiz.esq)
    print(raiz.dado, end=" ")
    if raiz.dir:
        inorder(raiz.dir)
    

def posorder(raiz):
    pass

def busca_largura(raiz):
    q = Queue()
    if not raiz:
        return
    
    q.push(raiz)
        
    while q.size() > 0:
        no = q.pop()
        print(no.dado, end=" ")
        if no.esq != None:
            q.push(no.esq)
        if no.dir != None:
            q.push(no.dir)
            
def bfs_invertido(raiz):
    q = Queue()
    l = []
    if not raiz:
        return
    q.push(raiz)
    while q.size() > 0:
        no = q.pop()
        l.append(no.dado)
        if no.esq:
            q.push(no.esq)
        if no.dir:
            q.push(no.dir)
    
    for i in reversed(l):
        print(i, end=" ")

    
        
raiz = NoArvoreBB(50)
raiz = insere(raiz, NoArvoreBB(17))
raiz = insere(raiz, NoArvoreBB(72))
raiz = insere(raiz, NoArvoreBB(12))
raiz = insere(raiz, NoArvoreBB(23))
raiz = insere(raiz, NoArvoreBB(54))
raiz = insere(raiz, NoArvoreBB(76))
raiz = insere(raiz, NoArvoreBB(9))
raiz = insere(raiz, NoArvoreBB(14))
raiz = insere(raiz, NoArvoreBB(19))
raiz = insere(raiz, NoArvoreBB(67))

busca_largura(raiz)
print('')
preorder(raiz)
print('')
inorder(raiz)
print()
bfs_invertido(raiz)