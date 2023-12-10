import math

n = int(input())
x_coelho, y_coelho = map(float, input().split())
x_raposa, y_raposa = map(float, input().split())
buracos = []

for i in range(n):
    x_buraco, y_buraco = map(float, input().split())
    buracos.append(x_buraco)
    buracos.append(y_buraco)

escapou = False  

for buraco in range(0, len(buracos), 2):
    db_coelho = math.sqrt((x_coelho - buracos[buraco]) ** 2 + (y_coelho - buracos[buraco + 1]) ** 2)
    db_raposa = math.sqrt((x_raposa - buracos[buraco]) ** 2 + (y_raposa - buracos[buraco + 1]) ** 2)
    
    if db_raposa > 2 * db_coelho and not escapou:
        print(f'O coelho pode escapar pelo buraco ({buracos[buraco]:.3f}, {buracos[buraco + 1]:.3f}).')
        escapou = True

if not escapou:
    print('O coelho nao pode escapar.')

        

