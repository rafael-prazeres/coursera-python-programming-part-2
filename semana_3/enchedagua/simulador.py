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


class Simulador:    
    def __init__(self, semente):
        random.seed(semente)
        capacidade = random.randrange(CAP_MIN, CAP_MAX)
        self.bal = Balde(capacidade)
        self.vol = 0
        self.avisou = False

    def sorteia(self):
        self.vol = random.randrange(VOL_MIN, VOL_MAX)
        print()
        print("Volume atual   : ", self.bal.volume)
        print("Volume sorteado: ", self.vol)
        return self.vol

    def deposita(self):
        '''
        adiciona o ultimo volume sorteado self.vol
        ao balde e retorna True se o
        balde estiver cheio e False caso contrario.
        '''
        self.bal.deposita(self.vol)
        if not self.avisou and self.bal.volume >= self.bal.capacidade/2:
            self.avisou = True
            print("volume atingiu ou ultrapassou a metade da capacidade.")
        return self.bal.cheio
        
    def finaliza(self):
        print("\nFim da simulacao")
        print("Capacidade do balde: %d" % self.bal.capacidade)
        print("Volume final: %d" % self.bal.volume)

        if self.bal.derramado > 0:
            print("Balde esta cheio e houve derramamento de agua")
            print("Volume derramado foi: %d" %(self.bal.derramado))
        else:
            if self.bal.cheio:
                print("Balde esta cheio e nao houve derramamento de agua")
            elif self.bal.capacidade - self.bal.volume >= self.vol:
                print("Balde nao esta cheio.")
                print("Havia espaco para o ultimo volume sorteado: %d" % self.vol)
            else:
                print("Balde nao esta cheio.")
                print("Nao havia espaco para o ultimo volume sorteado: %d" % self.vol)

if __name__ == "__main__":
    s = Simulador(123)
    v1 = s.sorteia()
    r1 = s.deposita()
    print(v1, r1)
    v2 = s.sorteia()
    r2 = s.deposita()
    print(v2, r2)
    s.finaliza()


