def dimensoes(matriz):
    return "{}X{}".format(len(matriz),len(matriz[0]))

def matrizes_mesma_dimensao(m1, m2):
    return dimensoes(m1) == dimensoes(m2)

def soma_matrizes(m1, m2):
    if matrizes_mesma_dimensao(m1, m2):
        matriz_soma = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m2[0])):
                linha.append(0)
            matriz_soma.append(linha)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                matriz_soma[i][j] = m1[i][j] + m2[i][j]
        return matriz_soma
    else:
        return False
