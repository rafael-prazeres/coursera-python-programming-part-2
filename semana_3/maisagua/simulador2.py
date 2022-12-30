'''
Módulo Simulador mantem o estado da simulacao e
os procedimentos para simular. Note que a classe
Simulador "esconde" o modulo random da funcao main.
'''

import random
from balde import Balde

# definicao de constantes
CAP_MIN = 10
CAP_MAX = 51 # ja ajustado ao random
VOL_MIN = 1
VOL_MAX = 11 # ja ajustado ao random


class Simulador2:    
    def __init__(self, semente):
        random.seed(semente)
        c1 = random.randrange(CAP_MIN, CAP_MAX)
        c2 = random.randrange(CAP_MIN, CAP_MAX)
        c3 = random.randrange(CAP_MIN, CAP_MAX)
        self.bal1 = Balde(c1)
        self.bal2 = Balde(c2)
        self.bal3 = Balde(c3)
        self.vol = 0
        self.avisou = False
        self.iteracao = 0
        self.descartes = 0


    def sorteia(self):
        self.vol = random.randrange(VOL_MIN, VOL_MAX)        
        return self.vol

    def descarta(self):
        self.iteracao += 1
        self.descartes += 1
        return False

    def deposita(self, escolha):
        '''
        Adiciona o ultimo volume sorteado self.vol
        ao balde escolhido e permite o depósito do volume
        excedente em outro balde, caso o balde inicialmente
        escolhido fique cheio.
        '''
        self.iteracao += 1
        print(". . . . . . . . . . . . . . . . . . . . .")
        print("Iteração: ", self.iteracao)
        print("Volumes ocupados: %s %s %s"%(self.bal1, self.bal2, self.bal3))
        print("Descartes: ", self.descartes)
        print("Quantidade disponibilizada: %s"%(self.vol))
        print("Opção desejada: %s"%(escolha))
                
        if escolha == 1:
            self.bal1.deposita(self.vol)
        if escolha == 2:
            self.bal2.deposita(self.vol)        
        if escolha == 3:
            self.bal3.deposita(self.vol)
        
        print("Volumes ocupados: %s %s %s"%(self.bal1, self.bal2, self.bal3))

        excedente_depositado = False

        if escolha == 1 and self.bal1.derramado > 0:
            if self.bal2.volume_livre() > 0 or self.bal2.volume_livre() > 0:
                while not excedente_depositado:
                    balde_deposito_excedente = int(input("Escolha recipiente para depositar excedente de 1:"))
                    if balde_deposito_excedente == 2:
                        self.bal2.deposita(self.bal1.derramado)
                        excedente_depositado = True
                    elif balde_deposito_excedente == 3:
                        self.bal3.deposita(self.bal1.derramado)
                        excedente_depositado = True
        if escolha == 2 and self.bal2.derramado > 0:
            if self.bal1.volume_livre() > 0 or self.bal3.volume_livre() > 0:
                while not excedente_depositado:
                    balde_deposito_excedente = int(input("Escolha recipiente para depositar excedente de 2:"))
                    if balde_deposito_excedente == 1:
                        self.bal1.deposita(self.bal2.derramado)
                        excedente_depositado = True
                    elif balde_deposito_excedente == 3:
                        self.bal3.deposita(self.bal2.derramado)
                        excedente_depositado = True
        if escolha == 3 and self.bal3.derramado > 0:
            if self.bal1.volume_livre() > 0 or self.bal2.volume_livre() > 0:
                while not excedente_depositado:
                    balde_deposito_excedente = int(input("Escolha recipiente para depositar excedente de 3:"))
                    if balde_deposito_excedente == 1:
                        self.bal1.deposita(self.bal3.derramado)
                        excedente_depositado = True
                    elif balde_deposito_excedente == 2:
                        self.bal2.deposita(self.bal3.derramado)
                        excedente_depositado = True

        print("Volumes ocupados: %s %s %s"%(self.bal1, self.bal2, self.bal3))
        if self.bal1.cheio and self.bal2.cheio and self.bal3.cheio:
            return True
        else:
            return False
        
    def finaliza(self):
        print("\nFim da simulacao")
        print("Volumes ocupados: %s %s %s"%(self.bal1, self.bal2, self.bal3))
        print("Capacidades: %s %s %s"%(self.bal1.capacidade, self.bal2.capacidade, self.bal3.capacidade))
        print("Capacidade total: %d" % (self.bal1.capacidade + self.bal2.capacidade + self.bal3.capacidade))
        print("Volume ocupado: %d" % (self.bal1.volume + self.bal2.volume + self.bal3.volume))
        print("Volume livre: %d" % (self.bal1.volume_livre() + self.bal2.volume_livre() + self.bal3.volume_livre()))
        print("Volume derramado: %d" % (self.bal1.derramado + self.bal2.derramado + self.bal3.derramado))
        print("Descartes: %s"%(self.descartes))
        print("--------------------------------")

if __name__ == "__main__":
    s = Simulador2(12)
    v1 = s.sorteia()
    s.deposita(1)
    s.deposita(2)
    s.deposita(3)
    print(v1, s.bal1, s.bal2, s.bal3)
    v2 = s.sorteia()
    s.deposita(1)
    s.deposita(2)
    s.deposita(3)
    print(v2, s.bal1, s.bal2, s.bal3)
    v3 = s.sorteia()
    s.deposita(1)
    s.deposita(2)
    s.deposita(3)
    print(v3, s.bal1, s.bal2, s.bal3)

    s.finaliza()


