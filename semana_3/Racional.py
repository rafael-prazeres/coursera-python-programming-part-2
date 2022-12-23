class Racional:
    def __init__(self, n=0, d=1):
        mdc = self.mdc(n,d)
        print("mdc = " + str(mdc))
        n = n / mdc
        d = d / mdc
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

    def mul(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Racional(n, d)

    def div(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return Racional(n, d)

    def add(self, other):
        d = self.den * other.den
        n = (d / self.den) * self.num + (d / other.den) * other.num
        return Racional(n, d)

    def sub(self, other):
        d = self.den * other.den
        print("d = " + str(d))
        n = (d / self.den) * self.num - (d / other.den) * other.num
        return Racional(n, d)

    def mdc(self, a, b):
        if a < b:
            mdc = a
        else:
            mdc = b
        print("mdc inside = " + str(mdc))
        while mdc > 1:
            if (a % mdc != 0 or b % mdc != 0):
                mdc -= 1
            else:
                break
        return mdc

r1 = Racional(2)
r2 = Racional(12,6)
print(r2)
print(r1, '*', r2, '=>', r1.mul(r2))
print(r1, '/', r2, '=>', r1.div(r2))
print(r1, '+', r2, '=>', r1.add(r2))
print(r1, '-', r2, '=>', r1.sub(r2))
