import random

class Ordenador:

    def sequencia_ordenada(self, seq):
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                return False
        return True

    def crescente(self, seq):
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                return False
        return True

    def gerar_sequencia(self, tamanho):

        return random.sample(range(-tamanho, tamanho), tamanho)
    
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo  = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # Colocar o menor elemento encontrado no início da sub-lista
            # Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    def insercao(self, seq):
        novo = 2
        while novo <= len(seq):
            for i in range(1,len(seq[:novo])):
                # print("i = ", i)
                if seq[novo - i] < seq[novo - i - 1]:
                    seq[novo - i], seq[novo - i - 1] = seq[novo - i - 1], seq[novo - i]
                    # print(seq[0:novo], sep=' ')
                else:
                    # print(seq[0:novo], sep=' ')
                    break
            novo += 1

    def bolha(self, seq):
        houve_troca = True
        while houve_troca == True:
            houve_troca = False
            for i in range(1, len(seq)):
                if seq[i] < seq[i - 1]:
                    seq[i], seq[i - 1] = seq[i - 1], seq[i]
                    houve_troca = True

    def bolha_video(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def busca_sequencial(self, lista, elemento):
        for i in range(len(lista)):
            print("O valor do elemento inspecionado é: ", elemento)
            if lista[i] == elemento:
                return i
        return False

    def busca_binaria(self, seq, x):
        '''
            (list, float) -> bool
            retorna a posicao em que x ocorre na lista ordenada,
            ou None caso contrario, usando o algoritmo de busca binaria.
        '''
        meio = len(seq) // 2
        
        if len(seq) > 0:

            if len(seq) % 2 > 0:
                if x == seq[meio]:
                    return meio
                elif x < seq[meio]:
                    primeira_metade = seq[:meio]
                    return self.busca_binaria(primeira_metade, x)
                else:
                    segunda_metade = seq[meio + 1:]
                    return self.busca_binaria(segunda_metade, x)
            else:
                if x == seq[meio]:
                    return meio
                elif x == seq[meio - 1]:
                    return meio - 1
                elif x < seq[meio]:
                    primeira_metade = seq[:meio]
                    return self.busca_binaria(primeira_metade, x)
                elif x > seq[meio - 1]:
                    segunda_metade = seq[meio:]
                    return self.busca_binaria(segunda_metade, x)
