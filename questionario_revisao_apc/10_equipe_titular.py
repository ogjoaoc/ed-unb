n = int(input())
jogadores = list(map(int, input().split()[:n]))
soma_titulares = 0
soma_reservas = 0
jogadores = sorted(jogadores, reverse=True)

for i in range(11):
    soma_titulares += jogadores[i]
    
if n > 22:
    for i in range(11, 22):
        soma_reservas += jogadores[i]
else:
    for i in range(11, n):
        soma_reservas += jogadores[i]
    
diferenca = soma_titulares - soma_reservas

print(diferenca)