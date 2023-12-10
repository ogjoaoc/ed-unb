n = int(input())
for i in range(n):
    count = 0
    count_not_in = 0
    plano = list(input())
    aux = plano
    tamanho_plano = len(plano)
    for j in range(3):
        plano_turno = list(input())
        for p in plano_turno:
            if p in plano and plano != []:
                aux.remove(p)
                count += 1
            else:
                count_not_in += 1
    
    if count_not_in > 0:
        print('You died!')
    elif count == tamanho_plano and count_not_in == 0:
        print("It's in the box!")
    elif count < tamanho_plano:
        print("Bora ralar:", end=" ")
        resposta = set("".join(sorted(aux)))
        a = sorted(resposta)
        print("".join(a))