def frequencia(mensagem):
        if mensagem == '':
            nada = ''
            return nada
        contagem = {}
    
        for caractere in mensagem:
            if caractere in contagem:
                contagem[caractere] += 1
            else:
                contagem[caractere] = 1

        caractere_mais_comum = 0
        contagem_maxima = 0

        for caractere, contagem_atual in contagem.items():
            if contagem_atual > contagem_maxima:
                caractere_mais_comum = caractere
                contagem_maxima = contagem_atual

        return caractere_mais_comum
    


