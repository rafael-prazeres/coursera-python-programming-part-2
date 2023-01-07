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

    def merge_sort(self, lista):
        if len(lista) <= 1:
            return lista
        meio = (len(lista))//2
        lado_esquerdo = self.merge_sort(lista[:meio])
        lado_direito = self.merge_sort(lista[meio:])
        return self.merge(lado_esquerdo, lado_direito)

    def merge(self, lado_esquerdo, lado_direito):
        if not lado_esquerdo:
            return lado_direito
        if not lado_direito:
            return lado_esquerdo
        if lado_esquerdo[0] < lado_direito[0]:
            return [lado_esquerdo[0]] + self.merge(lado_esquerdo[1:], lado_direito)
        return [lado_direito[0]] + self.merge(lado_esquerdo, lado_direito[1:])
