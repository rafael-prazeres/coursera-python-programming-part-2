"""
    Modulo Balde
    contem a classe balde e seus testes
"""

class Balde:
    '''
        A classe Balde modela um recipente com capacidade e
        volume atual. Ela armazena tambem o volume derramado e
        indica se esta cheio.
    '''

    def __init__(self, cap):
        self.capacidade = cap
        self.volume     = 0
        self.derramado  = 0
        self.cheio      = False

    def __str__(self):
        if self.cheio:
            s = "*{0:2d}*".format(self.volume)
        else:
            s = "[{0:2d}]".format(self.volume)
        return s

    def deposita(self, vol):
        '''
            Deposita um volume de agua vol e atualiza o estado do Balde.
        '''
        self.volume += vol
        if self.volume >= self.capacidade:
            self.cheio = True
            self.derramado = self.volume - self.capacidade
            self.volume = self.capacidade
        return self.volume

    def volume_livre(self):
        return self.capacidade - self.volume

if __name__ == "__main__":
    # programa de teste da classe Balde
    balde = Balde(10)
    d1 = balde.deposita(3)
    d2 = balde.deposita(4)
    print(balde)
    d3 = balde.deposita(5)
    print(balde)
    print(d1, d2, d3)
