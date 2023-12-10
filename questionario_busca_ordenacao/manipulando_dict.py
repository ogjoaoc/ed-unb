dados = []
i = 0
n = int(input())

while i < n:
    entrada = input()
    entrada_split = entrada.split()

    nome = entrada_split[0]
    sobrenome = entrada_split[1]
    altura = int(entrada_split[2])
    peso = int(entrada_split[3])

    dados.append({'nome': nome, 'sobrenome': sobrenome, 'altura': altura, 'peso': peso})
    i += 1

ordenada_por_altura_peso = sorted(dados, key=lambda x: (abs(180 - x['altura']), x['peso'] < 75, abs(75 - x['peso']), x['sobrenome'], x['nome']))

for pessoa in ordenada_por_altura_peso:
    print(f"{pessoa['sobrenome']}, {pessoa['nome']}")
