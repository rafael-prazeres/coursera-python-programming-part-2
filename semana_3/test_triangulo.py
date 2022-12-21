import Triangulo
import pytest

class TestTriangulo:

    @pytest.mark.parametrize("lados, tipo_triangulo", [
        ([4, 4, 4], "equilátero"),
        ([3, 4, 5], "escaleno"),
        ([3, 4, 3], "isósceles"),
        ([3, 3, 4], "isósceles"),
        ([4, 3, 3], "isósceles"),
        ])

    def test_tipo_lado(self, lados, tipo_triangulo):
        t = Triangulo.Triangulo(lados[0], lados[1], lados[2])
        assert t.tipo_lado() == tipo_triangulo
        
    @pytest.mark.parametrize("lados, retangulo", [
        ([5, 4, 3], True),
        ([3, 4, 5], True),
        ([4, 5, 3], True),
        ([6, 8, 10], True),
        ([2, 3, 4], False),
        ])

    def test_triangulo_retangulo(self, lados, retangulo):
        t = Triangulo.Triangulo(lados[0], lados[1], lados[2])
        assert t.retangulo() == retangulo

    @pytest.mark.parametrize("lados_t1, lados_t2, semelhantes", [
        ([3, 4, 5], [6, 8, 10], True),
        ([3, 4, 5], [10, 8, 6], True),
        ([5, 4, 3], [6, 8, 10], True),
        ([5, 5, 5], [5, 5, 5], True),
        ([1, 2, 3], [4, 5, 6], False),
        ])

    def test_triangulos_semelhantes(self, lados_t1, lados_t2, semelhantes):
        t1 = Triangulo.Triangulo(lados_t1[0], lados_t1[1], lados_t1[2])
        t2 = Triangulo.Triangulo(lados_t2[0], lados_t2[1], lados_t2[2])
        assert t1.semelhantes(t2) == semelhantes
