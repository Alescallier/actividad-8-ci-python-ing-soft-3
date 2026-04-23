from app import suma, resta, es_par, mayor_de_edad, saludar


def test_suma():
    assert suma(2, 3) == 5


def test_resta():
    assert resta(5, 2) == 3


def test_es_par():
    assert es_par(4) is True


def test_mayor_de_edad():
    assert mayor_de_edad(20) is True


def test_saludar():
    assert saludar("Ale") == "Hola, Ale"
