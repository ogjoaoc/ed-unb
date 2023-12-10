class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
p = Stack()
strlida = input()
aux = []

for i in range(len(strlida)):
    if strlida[i] != "*":
        p.push(strlida[i])
    else:
        aux.append(p.pop())

print("".join(aux))    