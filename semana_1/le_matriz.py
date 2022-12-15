#-------------------------------------------------------
def leia_matriz():
    '''(None) -> matriz (lista de listas)

    Funcao que le do teclado o numero n_linhas de linhas
    e o numero n_colunas de colunas e os elementos de
    uma matriz de inteiros dimensao n_linha x n_colunas.

    A funcao cria e retorna a matriz lida.
    '''
    # print("Vixe! Ainda nao fiz a funcao!")

    num_linhas = int(input("Digite o número de linhas: "))
    num_colunas = int(input("Digite o número de colunas: "))
    matriz = []
    for i in range(num_linhas):
        print("matriz = {}".format(matriz))
        linha = []
        for j in range(num_colunas):
            print("linha {} = {}".format(i,linha))
            valor = int(input("Digite o elemento ({},{}): ".format(i,j)))
            linha.append(valor)
        matriz.append(linha)
        
    return matriz

    
#-----------------------------------------------------
# teste
a_mat = leia_matriz()
print(a_mat)
