def imprime_matriz(m):
    num_linhas = len(m)
    num_colunas = len(m[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            if j == num_colunas - 1:
                print(m[i][j])
            else:
                print(m[i][j], end=" ")
