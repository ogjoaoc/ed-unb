n = int(input())
pessoa = []
i = 0

while i < n:
    entrada_split = input().split()
    nome = entrada_split[0]
    sobrenome = entrada_split[1]
    altura = int(entrada_split[2])
    peso = int(entrada_split[3])
    
    pessoa.append({'nome': nome, 'sobrenome': sobrenome, 'altura': altura, 'peso': peso})
    i += 1
    
pessoa_ordenada_por_altura = sorted(pessoa, key=lambda x: abs(180 - x['altura']))

print(pessoa_ordenada_por_altura)    
    