class Racional:
    def __init__(self, n=0, d=1):
        mdc = self.mdc(n,d)
        print("mdc= {0}".format(mdc))
        n = n // mdc
        d = d // mdc
        self.put(n, d)

    def __str__(self):
        if self.den == 1:
            return "%d"%(self.num)
        else:
            return "%d/%d"%(self.num, self.den)

    def get(self):
        return self.num, self.den

    def put(self, n=0, d=1):
        self.num, self.den = n, d

    def __mul__(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Racional(n, d)

    def __truediv__(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return Racional(n, d)

    def __add__(self, other):
        d = self.den * other.den
        n = (d / self.den) * self.num + (d / other.den) * other.num
        return Racional(n, d)

    def __sub__(self, other):
        d = self.den * other.den
        n = (d / self.den) * self.num - (d / other.den) * other.num
        return Racional(n, d)

    def mdc(self, a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a

r1 = Racional(8,12)
r2 = Racional(3,9)
print(r1)
print(r2)
print(r1, '*', r2, '=>', r1 * r2)
print(r1, '/', r2, '=>', r1 / r2)
print(r1, '+', r2, '=>', r1 + r2)
print(r1, '-', r2, '=>', r1 - r2)
