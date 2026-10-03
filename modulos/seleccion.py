# Seleccionar, retirar y ver cursos de la selección

from data.cursos_data import CREDITOS_MAXIMOS
from modulos.matricula import esta_confirmada
from modulos.utilidades import clave_horario, formato_horario, imprimir_titulo
from modulos.validaciones import obtener_curso, total_creditos, validar_curso

_MENSAJE_BLOQUEO = ("Su matrícula ya fue confirmada y no puede modificarse. "
                    "Anule la confirmación para realizar cambios.")


def seleccionar_curso(codigo, seleccionados):
    """Agrega un curso a la selección solo si cumple prerrequisito, créditos y horario."""
    if esta_confirmada():
        print(_MENSAJE_BLOQUEO)
        return False

    curso = obtener_curso(codigo)
    if curso is None:
        print("El curso no existe")
        return False

    if any(sel["codigo"] == codigo for sel in seleccionados):
        print("El curso ya está seleccionado")
        return False

    errores = validar_curso(curso, seleccionados)
    if errores:
        print(f"No se puede seleccionar {codigo} - {curso['nombre']}:")
        for error in errores:
            print(f"  ✗ {error}")
        return False

    seleccionados.append(curso)
    print("Curso seleccionado correctamente")
    print(f"Créditos acumulados: {total_creditos(seleccionados)} / {CREDITOS_MAXIMOS}")
    return True


def retirar_curso(codigo, seleccionados):
    """Quita un curso de la selección actual."""
    if esta_confirmada():
        print(_MENSAJE_BLOQUEO)
        return False

    for curso in seleccionados:
        if curso["codigo"] == codigo:
            seleccionados.remove(curso)
            print(f"Curso {codigo} - {curso['nombre']} retirado de su selección")
            print(f"Créditos acumulados: {total_creditos(seleccionados)} / {CREDITOS_MAXIMOS}")
            return True

    print("El curso no está en su selección")
    return False


def ver_seleccion(seleccionados):
    """Muestra los cursos seleccionados ordenados por día y hora, con el total de créditos."""
    imprimir_titulo("MI SELECCIÓN ACTUAL")

    if not seleccionados:
        print("Aún no ha seleccionado ningún curso.")
        return

    print()
    for curso in sorted(seleccionados, key=clave_horario):
        print(f"[{curso['codigo']}] {curso['nombre']}")
        print(f"   Créditos: {curso['creditos']} | Prerrequisito: {curso['prerrequisito']}")
        print(f"   Horario: {formato_horario(curso)}")
        print("-" * 54)

    creditos = total_creditos(seleccionados)
    print(f"Cursos seleccionados: {len(seleccionados)}")
    print(f"Créditos acumulados: {creditos} / {CREDITOS_MAXIMOS}")
    print(f"Créditos aún disponibles: {max(CREDITOS_MAXIMOS - creditos, 0)}")
    print("Estado: CONFIRMADA" if esta_confirmada() else "Estado: PROVISIONAL (sin confirmar)")
