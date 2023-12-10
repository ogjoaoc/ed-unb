def fib(n):
    chamadas.append(n)
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input())
chamadas = []
ans = fib(n)

print(f'fibonacci({n}) = {ans}.')
for i in range(n+1):
    print(f'{chamadas.count(i)} chamada(s) a fibonacci({i}).')
