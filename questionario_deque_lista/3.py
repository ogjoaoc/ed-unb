def exibe_candidatos(deque, pos, ordem):
    d2 = Deque()
    if ordem == "direta":
        for i in range(pos):
            deque.remove_rear()
        for k in range(deque.size()):
            print(deque.remove_rear())
    else:
        for j in range(pos+1):
            d2.add_rear(deque.remove_front())
        
        for l in range(d2.size()):
            print(d2.remove_rear())
         