# Generar horario automáticamente
#
# Propuesta rápida con un algoritmo voraz: recorre la oferta disponible en orden
# y se queda con cada curso que aún cabe (créditos) y no se cruza con los ya elegidos.
# No garantiza la mejor combinación; para eso está el optimizador (backtracking).

from data.cursos_data import CREDITOS_MAXIMOS
from modulos.utilidades import clave_horario, formato_horario, imprimir_titulo
from modulos.validaciones import hay_cruce, obtener_cursos_disponibles


def generar_horario():
    cursos_disponibles = obtener_cursos_disponibles()

    matricula = []
    creditos = 0

    for curso in cursos_disponibles:

        if creditos + curso["creditos"] > CREDITOS_MAXIMOS:
            continue

        if any(hay_cruce(curso, matriculado) for matriculado in matricula):
            continue

        matricula.append(curso)
        creditos += curso["creditos"]

    imprimir_titulo("HORARIO AUTOMÁTICO GENERADO")

    if not matricula:
        print("No se pudo generar una matrícula.")
        return matricula

    for curso in sorted(matricula, key=clave_horario):
        print(f"{curso['codigo']} - {curso['nombre']} | {formato_horario(curso)}")

    print(f"\nTotal de créditos: {creditos} / {CREDITOS_MAXIMOS}")
    return matricula
