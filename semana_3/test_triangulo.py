import Triangulo
import pytest

class TestTriangulo:

    def test_equilatero(self):
        t = Triangulo.Triangulo(4, 4, 4)
        assert t.tipo_lado() == "equilátero"

    def test_escaleno(self):
        t = Triangulo.Triangulo(3, 4, 5)
        assert t.tipo_lado() == "escaleno"

    def test_isosceles_ac(self):
        t = Triangulo.Triangulo(3, 4, 3)
        assert t.tipo_lado() == "isósceles"

    def test_isosceles_ab(self):
        t = Triangulo.Triangulo(3, 3, 4)
        assert t.tipo_lado() == "isósceles"

    def test_isosceles_bc(self):
        t = Triangulo.Triangulo(4, 3, 3)
        assert t.tipo_lado() == "isósceles"
