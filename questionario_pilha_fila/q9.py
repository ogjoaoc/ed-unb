class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def enqueue_inferno(self, item):
        self.items.insert(len(self.items), item)
    
f = Queue()

fila = list(input().split(" "))
avancos = int(input())

for k in range(len(fila)):
    f.enqueue(fila[k])
    
if avancos != 0:
    for i in range(avancos):
        f.enqueue_inferno(f.dequeue())
    
print(f'Pessoa da frente: {f.items[-1]}')
print(f'Pessoa do fim: {f.items[0]}')