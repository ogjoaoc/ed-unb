class Queue():
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

q = Queue()

n = input().split(" ")

n_veiculos = int(n[0])
f = int(n[1])
limite_peso = n[2]
contador = 0

veiculos = list(input().split(" "))

i = 0
while i < len(veiculos):
    veiculos[i] = int(veiculos[i])
    if f == 1:
        if veiculos[i] < limite_peso:
            q.push(veiculos[i])
            contador += 5
        else:
            contador += 10
        i += 1
    if f == 2:
        if veiculos[i] < limite_peso:
            q.push(veiculos[i])
            contador += 5
        else:
            contador += 10
            i += 2
    if f == 3:
        if veiculos[i] < limite_peso:
            q.push(veiculos[i])
            contador += 5
        else:
            contador += 10
            i += 3

print(contador)
            
    