import buscador
import pytest
import ordenador

class TestaBuscador:
    
    @pytest.fixture
    def b(self):
        return buscador.Buscador()

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    def gerar_sequencia(self, n):
        return [x for x in range(10,n,10)]

    @pytest.mark.parametrize("elemento, indice",[
        (10,0),
        (20,1),
        (30,2),
        (40,3),
        (50,4),
        (60,5),
        (70,6),
        (80,7),
        (90,8),
        (100,False),
        (-10,False),
        (15,False),
        ])
    def testa_busca_binaria_recursiva(self, b, elemento, indice):
        lista = self.gerar_sequencia(100)
        assert b.busca_binaria_recursiva(lista,elemento) == indice
    
