import random
import time
import ordenador
import buscador

class ContaTempos:

    def lista_aleatoria(self, n):
        lista = [random.randrange(n) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara_buscador(self, n, x):
        lista1 = self.lista_aleatoria(n)
        o = ordenador.Ordenador()
        o.selecao_direta(lista1)
        b = buscador.Buscador()

        antes = time.time()
        i = b.busca_sequencial(lista1, x)
        depois = time.time()
        tempo_sequencial = depois - antes
        print("Busca sequencial demorou ", tempo_sequencial, " e retornou ", i)

        antes = time.time()
        i = b.busca_binaria(lista1, x)
        depois = time.time()
        tempo_binaria = depois - antes
        print("Busca binária demorou ", tempo_binaria, " e retornou ", i)

        print(tempo_binaria > tempo_sequencial)
        

    def compara_ordenador(self, n):

        o = ordenador.Ordenador()

        print("Comprara com listas aleatórias")

        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)

        antes = time.time()
        o.insercao(lista3)
        depois = time.time()
        print("Inserção direta demorou ", depois - antes)

        print("\nComprara com listas quase ordenadas")

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)

        antes = time.time()
        o.insercao(lista3)
        depois = time.time()
        print("Inserção direta demorou ", depois - antes)

