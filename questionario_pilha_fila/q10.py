class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        if item == "(":
            self.items.append(item)
            return True
        else:
            self.items.append(item)
            return False
            
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

p = Stack()    
n = int(input())
i = 0
while i < n:
    expressao = list(input())
    flag = False
    k = 0
    count = 0
    while (k < len(expressao)):
        flag = p.push(expressao[k])
        if count == 2:
            break
        if flag:
            count += 1
        k += 1
    
    if count >= 2:
        print("A expressão possui duplicata.")
    else:
        print("A expressão não possui duplicata.")
    
    i += 1
    