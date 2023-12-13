def add_inicio(pos, item):
    temp = Node(item)
    temp.setNext(lista.head)
    lista.head = temp
    
def buscar(lista, item):
    current = lista.head
    found = False
    previous = None
    while current != None and not found:
        if current.getData() == item:
            next_temp = current.getNext()
            temp = lista.head
            lista.head = Node(item)
            lista.head.setNext(temp)
            previous.setNext(next_temp)
            found = True
        else:
            previous = current
            current = current.getNext()
    
    if found:
        return item
    else:
        return None