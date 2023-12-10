# cpy patch
import math
tamanho_total = int(input())
print(f'Transmitindo {tamanho_total} bytes...')

taxas = []  
total_transmitido = 0
tempo_total = 0

while total_transmitido < tamanho_total:
    taxa_intervalo = 0

    for i in range(5):
        taxa = int(input())
        taxas.append(taxa)  
        total_transmitido += taxa  
        taxa_intervalo += taxa  
        tempo_total += 1
        
        if total_transmitido >= tamanho_total:
            break 
            
    if total_transmitido >= tamanho_total:
        break  

    if (taxa_intervalo / 5) == 0:
        print('Tempo restante: pendente...')
    else:
        tempo_intervalo = 5 * (tamanho_total - total_transmitido) / taxa_intervalo
        if tempo_intervalo > 0:
            tempo_intervalo = math.ceil(tempo_intervalo)
            print(f"Tempo restante: {tempo_intervalo} segundos.")
    
print(f"Tempo total: {tempo_total} segundos.")

