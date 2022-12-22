class Complexo:
    
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def soma(self, c2):
        return Complexo(self.a + c2.a, self.b + c2.b)

    def multiplicacao(self, c2):
        return Complexo((self.a*c2.a - self.b*c2.b), (self.a*c2.b + c2.a*self.b))

    def __str__(self):
        if self.a != 0 and self.b > 0:
            return "{0}+{1}i".format(self.a, self.b)
        elif self.a != 0 and self.b < 0:
            return "{0}{1}i".format(self.a, self.b)
        elif self.a == 0 and self.b != 0:
            return "{0}i".format(self.b)
        elif self.a != 0 and self.b == 0:
            return "{0}".format(self.a)
        else:
            return "{0}".format(0)
