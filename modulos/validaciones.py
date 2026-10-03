# Reglas de negocio: prerrequisitos, límite de créditos y cruces de horario

from data.cursos_data import cursos, cursos_llevados, CREDITOS_MAXIMOS
from modulos.utilidades import formato_horario


def obtener_curso(codigo):
    """Búsqueda lineal de un curso por su código. Devuelve None si no existe."""
    for curso in cursos:
        if curso["codigo"] == codigo:
            return curso
    return None


def verificar_prerrequisito(curso):
    prerrequisito = curso["prerrequisito"]
    return prerrequisito == "Ninguno" or prerrequisito in cursos_llevados


def hay_cruce(curso1, curso2):
    """Dos cursos se cruzan si coinciden en el día y sus horas se superponen."""
    if curso1["dia"] != curso2["dia"]:
        return False
    return curso1["hora_inicio"] < curso2["hora_fin"] and curso2["hora_inicio"] < curso1["hora_fin"]


def total_creditos(lista):
    return sum(curso["creditos"] for curso in lista)


def obtener_cursos_disponibles():
    """Cursos que el estudiante puede llevar: no aprobados y con prerrequisito cumplido."""
    return [
        curso for curso in cursos
        if curso["codigo"] not in cursos_llevados and verificar_prerrequisito(curso)
    ]


def validar_curso(curso, seleccionados):
    """Devuelve la lista de condiciones que impiden agregar `curso` a la selección."""
    errores = []

    if curso["codigo"] in cursos_llevados:
        errores.append("Ya aprobó este curso anteriormente.")

    if not verificar_prerrequisito(curso):
        requisito = obtener_curso(curso["prerrequisito"])
        detalle = f" ({requisito['nombre']})" if requisito else ""
        errores.append(f"No cumple el prerrequisito: {curso['prerrequisito']}{detalle}.")

    actual = total_creditos(seleccionados)
    nuevo_total = actual + curso["creditos"]
    if nuevo_total > CREDITOS_MAXIMOS:
        errores.append(
            f"Supera el límite de créditos: {actual} + {curso['creditos']} = "
            f"{nuevo_total} (máximo {CREDITOS_MAXIMOS})."
        )

    for otro in seleccionados:
        if hay_cruce(curso, otro):
            errores.append(
                f"Cruce de horario con {otro['codigo']} - {otro['nombre']} ({formato_horario(otro)})."
            )

    return errores


def validar_matricula(lista):
    """Revisa una matrícula completa. Devuelve la lista de incumplimientos (vacía si es válida)."""
    errores = []

    vistos = set()
    for curso in lista:
        codigo = curso["codigo"]
        if codigo in vistos:
            errores.append(f"El curso {codigo} está repetido.")
        vistos.add(codigo)

        if codigo in cursos_llevados:
            errores.append(f"{codigo} - {curso['nombre']}: ya fue aprobado anteriormente.")
        if not verificar_prerrequisito(curso):
            errores.append(
                f"{codigo} - {curso['nombre']}: no cumple el prerrequisito {curso['prerrequisito']}."
            )

    total = total_creditos(lista)
    if total > CREDITOS_MAXIMOS:
        errores.append(f"El total de créditos ({total}) supera el máximo permitido ({CREDITOS_MAXIMOS}).")

    for i, curso in enumerate(lista):
        for otro in lista[i + 1:]:
            if hay_cruce(curso, otro):
                errores.append(
                    f"Cruce de horario entre {curso['codigo']} ({formato_horario(curso)}) "
                    f"y {otro['codigo']} ({formato_horario(otro)})."
                )

    return errores
