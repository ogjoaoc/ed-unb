class Deque:
    def __init__(self):
        self.items = []
    
    def addFrente(self, item):
        self.items.insert(0, item)
    
    def addFinal(self, item):
        self.items.append(item)
        
    def removeInicio(self, item):
        return self.items.pop(0)
    
    def removeFinal(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    
d = Deque()
    
n = input().split(" ")
tam_sequencia = int(n[0])
passada = int(n[1])
sequencia = list(input().split())
aux = []
count = 0


for i in range(len(sequencia)-passada+1):
    for k in range(passada):
        d.addFinal(sequencia[k])
        
    sequencia.pop(0)
        
    for k in range(passada):
        aux.append(int(d.removeFinal()))

    media = (sum(aux))/passada
    print(int(media))
    aux = []
    

    
    