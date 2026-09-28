# Opcion 6 (Generar y visualizar el horario semana)
from data.cursos_data import cursos, cursos_llevados, CREDITOS_MAXIMOS


def verificar_prerrequisito(curso):
    prerrequisito = curso["prerrequisito"]

    if prerrequisito == "Ninguno":
        return True

    if prerrequisito in cursos_llevados:
        return True

    return False


def obtener_cursos_disponibles():
    disponibles = []

    for curso in cursos:

        if curso["codigo"] in cursos_llevados:
            continue

        if verificar_prerrequisito(curso):
            disponibles.append(curso)

    return disponibles


def hay_cruce(curso1, curso2):

    if curso1["dia"] != curso2["dia"]:
        return False

    if curso1["hora_inicio"] < curso2["hora_fin"] and \
       curso2["hora_inicio"] < curso1["hora_fin"]:
        return True

    return False


def generar_horario():

    cursos_disponibles = obtener_cursos_disponibles()

    matricula = []
    creditos = 0

    for curso in cursos_disponibles:

        if creditos + curso["creditos"] > CREDITOS_MAXIMOS:
            continue


        hay_conflicto = False

        for curso_matriculado in matricula:

            if hay_cruce(curso, curso_matriculado):
                hay_conflicto = True
                break

        if hay_conflicto:
            continue

        matricula.append(curso)
        creditos += curso["creditos"]

    print("\n╔════════════════════════════════════════════╗")
    print("║       HORARIO AUTOMÁTICO GENERADO         ║")
    print("╚════════════════════════════════════════════╝")

    if len(matricula) == 0:
        print("No se pudo generar una matrícula.")
        return

    for curso in matricula:
        print(
            f"{curso['codigo']} - {curso['nombre']} | "
            f"{curso['dia']} | "
            f"{curso['hora_inicio']:.2f} - {curso['hora_fin']:.2f}"
        )

    print(f"\nCréditos matriculados: {creditos}")