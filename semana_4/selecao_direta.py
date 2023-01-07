import random

class Ordenador:

    def sequencia_ordenada(self, seq):
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
