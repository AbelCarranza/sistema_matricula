# Resumen de matrícula

from data.cursos_data import CREDITOS_MAXIMOS
from modulos.utilidades import clave_horario, formato_horario, imprimir_titulo


def mostrar_resumen(seleccionados, confirmada=False):
    """Muestra el detalle de los cursos, horarios, el total de créditos y el estado de la matrícula."""
    imprimir_titulo("RESUMEN DE MATRÍCULA")

    if not seleccionados:
        print("⚠️ No tienes ningún curso seleccionado en tu matrícula.")
        return

    total_creditos = 0

    for curso in sorted(seleccionados, key=clave_horario):
        total_creditos += curso['creditos']
        print(f"• [{curso['codigo']}] {curso['nombre']} - {curso['creditos']} créditos")
        print(f"  Horario: {formato_horario(curso)}")

    print("-" * 54)
    print(f"Total de cursos seleccionados: {len(seleccionados)}")
    print(f"Total de créditos acumulados: {total_creditos} / {CREDITOS_MAXIMOS}")

    if confirmada:
        print("Estado de la matrícula: CONFIRMADA")
    else:
        print("Estado de la matrícula: PROVISIONAL (sin confirmar)")


def ver_resumen(seleccionados, confirmada):
    """El resumen solo está disponible cuando la matrícula está confirmada."""
    if not confirmada:
        imprimir_titulo("RESUMEN DE MATRÍCULA")
        print("El resumen estará disponible una vez que confirme su matrícula.")
        return

    mostrar_resumen(seleccionados, confirmada=True)
