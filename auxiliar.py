def filtroPreguntas(respuesta):
    respuestaFiltrada = respuesta.lower()
    if (
        respuestaFiltrada == "si"
        or respuestaFiltrada == "yes"
        or respuestaFiltrada == "afirmativo"
    ):
        return True
    else:
        return False
