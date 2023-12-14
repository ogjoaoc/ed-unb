class Deque:
    def __init__(self):
        self.items = []
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeRear(self):
        return self.items.pop(0)
        
    def removeFront(self):
        return self.items.pop()
    
    def addFront(self, item):
        self.items.append(item)
    
    def size(self):
        return len(self.items)
    
    def imprime(self):
        for k in self.items:
            print(k, end="")
        
d = Deque()

t = list(input())
ans = []

for i in t:
    if i in "0123456789":
        d.addFront(i)
    elif i == "*":
        ans.append(d.removeRear())
    elif i == "+":
        ans.append(d.removeFront())
    else:
        d.addRear(i)

for k in ans:
    print(k, end="")