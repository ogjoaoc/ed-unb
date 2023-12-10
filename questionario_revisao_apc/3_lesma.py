n = int(input())
lesmas = {'classeA': None, 'classeB': None, 'classeC': None}

for i in range(n):
    velocidade = int(input())

    if velocidade < 10 and (lesmas['classeA'] is None or velocidade > lesmas['classeA']):
        lesmas['classeA'] = velocidade
    elif 10 <= velocidade < 20 and (lesmas['classeB'] is None or velocidade > lesmas['classeB']):
        lesmas['classeB'] = velocidade
    elif velocidade > 20 and (lesmas['classeC'] is None or velocidade > lesmas['classeC']):
        lesmas['classeC'] = velocidade

print(lesmas['classeA'] or 0, lesmas['classeB'] or 0, lesmas['classeC'] or 0)
