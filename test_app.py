from app import (
    calcular_prioridad,
    carga_es_recomendada,
    calcular_costo_estimado,
    validar_espacio,
    estado_publicacion,
)


def test_calcular_prioridad_alta():
    resultado = calcular_prioridad("alta", 250, 80, 4.5)
    assert resultado == 100


def test_carga_es_recomendada():
    assert carga_es_recomendada(75) is True


def test_carga_no_recomendada():
    assert carga_es_recomendada(50) is False


def test_calcular_costo_estimado():
    assert calcular_costo_estimado(300, 1200) == 360000


def test_validar_espacio_suficiente():
    assert validar_espacio(80, 60) is True


def test_validar_espacio_insuficiente():
    assert validar_espacio(30, 50) is False


def test_estado_publicacion_disponible():
    assert estado_publicacion(True) == "Disponible"
