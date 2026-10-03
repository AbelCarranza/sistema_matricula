# Confirmar / Anular matrícula
#
# Antes de confirmar se vuelve a validar toda la selección (prerrequisitos, límite de
# créditos y cruces de horario) y se muestra el resumen final. Una matrícula con
# incumplimientos no puede confirmarse. Una vez confirmada, la selección queda bloqueada
# hasta que el estudiante anule la confirmación.

from modulos.resumen import mostrar_resumen
from modulos.utilidades import imprimir_titulo, pedir_si_no
from modulos.validaciones import validar_matricula

_estado = {"confirmada": False}


def esta_confirmada():
    return _estado["confirmada"]


def confirmar_matricula(seleccionados):
    imprimir_titulo("CONFIRMAR / ANULAR MATRÍCULA")

    if esta_confirmada():
        print("Su matrícula se encuentra confirmada.")
        mostrar_resumen(seleccionados, confirmada=True)
        if pedir_si_no("\n¿Desea anular la confirmación para modificar su selección? (s/n): "):
            _estado["confirmada"] = False
            print("Confirmación anulada. Puede modificar su selección y volver a confirmar.")
        return False

    if not seleccionados:
        print("⚠️ No tiene cursos seleccionados.")
        return False

    errores = validar_matricula(seleccionados)
    if errores:
        print("No es posible confirmar la matrícula. Corrija lo siguiente:")
        for error in errores:
            print(f"  ✗ {error}")
        return False

    mostrar_resumen(seleccionados)

    if not pedir_si_no("\n¿Confirmar su matrícula? (s/n): "):
        print("Confirmación cancelada.")
        return False

    _estado["confirmada"] = True
    print("\n✅ Matrícula confirmada correctamente.")
    return True
