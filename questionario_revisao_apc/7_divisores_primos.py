def verifPrimo(num):
    if num < 1:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

def primos_gemeos(n):
    lista_gemeos = []
    num = 3  
    while len(lista_gemeos) < n:
        if verifPrimo(num) and verifPrimo(num + 2):
            lista_gemeos.append((num, num + 2))
        num += 2
        
    return lista_gemeos