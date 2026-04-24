def calcular_prioridad(urgencia, distancia_km, espacio_disponible, reputacion):
    puntaje = 0

    if urgencia == "alta":
        puntaje += 40
    elif urgencia == "media":
        puntaje += 25
    else:
        puntaje += 10

    if distancia_km <= 300:
        puntaje += 25
    elif distancia_km <= 700:
        puntaje += 15
    else:
        puntaje += 5

    if espacio_disponible >= 70:
        puntaje += 20
    elif espacio_disponible >= 40:
        puntaje += 10

    if reputacion >= 4:
        puntaje += 15
    elif reputacion >= 3:
        puntaje += 8

    return puntaje


def carga_es_recomendada(puntaje):
    return puntaje >= 70


def calcular_costo_estimado(distancia_km, precio_por_km):
    return distancia_km * precio_por_km


def validar_espacio(espacio_disponible, espacio_requerido):
    return espacio_disponible >= espacio_requerido


def estado_publicacion(carga_activa):
    if carga_activa:
        return "Disponible"
    return "No disponible"
