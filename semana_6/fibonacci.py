def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Sequência de Fibonacci
# 1 1 2 3 5 8 13 21 34 55 89

import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144)
    ])

def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado

