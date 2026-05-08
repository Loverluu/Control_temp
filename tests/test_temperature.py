import pytest
from temperature import esta_en_alarma

def test_temperatura_alta():
    assert esta_en_alarma(90) is True

def test_temperatura_normal():
    assert esta_en_alarma(60) is False

def test_temperatura_invalida():
    with pytest.raises(ValueError):
        esta_en_alarma(-5)