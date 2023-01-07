import random

class Buscador:

    def gerar_sequencia(self, tamanho):
        return random.sample(range(-tamanho, tamanho), tamanho)
    
    def busca_sequencial(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1

    def busca_binaria_bugada(self, seq, x):
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
