#descompressao
n = int(input())
contador = 0
while contador < n:
    string_recebida = input()
    saida = ""
    current_letter = ""
    current_number = ""
    for char in string_recebida:
        if char.isalpha():
            if current_letter and current_number:
                saida += current_letter * int(current_number)
                current_letter = ""
                current_number = ""
            current_letter = char
        else:
            current_number += char
    if current_letter and current_number:
        saida += current_letter * int(current_number)
    print(saida)
    contador += 1