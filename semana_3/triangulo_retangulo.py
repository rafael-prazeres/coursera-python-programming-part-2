class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif self.a != self.b and self.b != self.c and self.a != self.c:
            return "escaleno"
        else:
            return "isósceles"

    def retangulo(self):
        hipotenusa = self.a
        cateto_b = self.b
        cateto_c = self.c
        if self.b > hipotenusa:
            hipotenusa, cateto_b = self.b, hipotenusa
        if self.c > hipotenusa:
            hipotenusa, cateto_c = self.c, hipotenusa
        return hipotenusa**2 == (cateto_b**2 + cateto_c**2)
