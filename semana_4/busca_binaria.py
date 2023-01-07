def busca_binaria(seq, x):
    '''
        (list, float) -> bool
        retorna a posicao em que x ocorre na lista ordenada,
        ou None caso contrario, usando o algoritmo de busca binaria.
    '''
    meio = len(seq) // 2
    # print("meio = ", meio)
    # print("tamanho seq = ", len(seq))
    print("O valor do elemento inspecionado é: ", x)
    
    if len(seq) > 0:

        if len(seq) % 2 > 0:
            if x == seq[meio]:
                # print("entrou len(seq) % 2 > 0")
                return meio
            elif x < seq[meio]:
                # print("entrou na primeira metade caso len(seq) % 2 > 0")
                primeira_metade = seq[:meio]
                # print(primeira_metade)
                return busca_binaria(primeira_metade, x)
            else:
                # print("entrou segunda metade caso len(seq) % 2 > 0")
                segunda_metade = seq[meio + 1:]
                # print(segunda_metade)
                return busca_binaria(segunda_metade, x)
        else:
            # print("seq meio = ", seq[meio])
            # print("seq meio - 1 = ", seq[meio - 1])
            # print("x = ", x)
            if x == seq[meio]:
                # print("entrou len(seq) % 2 == 0")
                return meio
            elif x == seq[meio - 1]:
                return meio - 1
            elif x < seq[meio]:
                # print("entrou na primeira metade caso len(seq) % 2 == 0")
                primeira_metade = seq[:meio]
                # print(primeira_metade)
                return busca_binaria(primeira_metade, x)
            elif x > seq[meio - 1]:
                # print("entrou na segunda metade caso len(seq) % 2 == 0")
                segunda_metade = seq[meio:]
                # print(segunda_metade)
                return busca_binaria(segunda_metade, x)

# escreva alguns testes da funcao busca_binaria

seq = [4, 10, 80, 90, 91, 93, 99, 100, 101]
testes = [4, 10, 101]

for t in testes:
    pos = busca_binaria(seq, t)
    # print("pos = ", pos)
    if pos is None:
        print("Nao achei ", t)
    else:
        print("Achei ", t)
