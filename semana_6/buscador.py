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

    def busca_binaria_recursiva(self, lista, elemento, min=0, max=None):
        '''
            (list, float) -> bool
            retorna a posicao em que o elemento ocorre na lista ordenada,
            ou False caso contrario, usando o algoritmo de busca binaria.
        '''
        if max == None:
            max = len(lista)-1
        if max < min:
            return False
        else:
            meio = min + (max-min)//2
        if lista[meio] > elemento:
            return self.busca_binaria_recursiva(lista, elemento, min, meio-1)
        elif lista[meio] < elemento:
            return self.busca_binaria_recursiva(lista, elemento, meio+1, max)
        else:
            return meio
        
