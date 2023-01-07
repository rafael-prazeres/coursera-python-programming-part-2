import ordenador
import pytest
import conta_tempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = conta_tempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = conta_tempos.ContaTempos()
        return c.lista_aleatoria(100)

    def test_bolha_l_aleatoria(self, o, l_aleatoria):
        o.bolha(l_aleatoria)
        assert o.sequencia_ordenada(l_aleatoria)

    def test_bolha_l_quase(self, o, l_quase):
        o.bolha(l_quase)
        assert o.sequencia_ordenada(l_quase)

    def test_selecao_direta_l_aleatoria(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert o.sequencia_ordenada(l_aleatoria)

    def test_selecao_direta_l_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert o.sequencia_ordenada(l_quase)

    def test_insercao_l_aleatoria(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert o.sequencia_ordenada(l_aleatoria)

    def test_insercao_l_quase(self, o, l_quase):
        o.insercao(l_quase)
        assert o.sequencia_ordenada(l_quase)
