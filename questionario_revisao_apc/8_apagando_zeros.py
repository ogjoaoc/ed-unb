n = int(input())  

for _ in range(n):
    string_recebida = input()
    zeros_to_remove = 0
    contador_de_zeros_entre_uns = 0
    sequencia = False

    for char in string_recebida:
        if char == '1':
            zeros_to_remove += contador_de_zeros_entre_uns
            contador_de_zeros_entre_uns = 0
            sequencia = True
        elif sequencia:
            contador_de_zeros_entre_uns += 1

    print(zeros_to_remove)

