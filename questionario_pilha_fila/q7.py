class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    
    
p1 = Stack()
p2 = Stack()

roupas = []
cores = []

n = int(input())
i = 0
contador_roupa = 0

while i < n:
    roupa = input().split(" ")
    p1.push(roupa[0])
    p2.push(roupa[1])
    roupa[2] = int(roupa[2])
    contador_roupa += roupa[2]
    i += 1
    
for k in range(n):
    roupas.append(p1.pop())
    cores.append(p2.pop())

for j in range(n):
    print(f'Tipo: {roupas[j]}, Cor: {cores[j]}')


print(f'Total de roupas: {n}')
print(f'Total de tempo: {contador_roupa}')