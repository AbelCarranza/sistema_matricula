from data.cursos_data import CREDITOS_MAXIMOS
from modulos.consulta import mostrar_cursos, buscar_curso, ver_curso_pre, mostrar_cursos_llevados
from modulos.seleccion import seleccionar_curso, ver_seleccion, retirar_curso
from modulos.automatico import generar_horario
from modulos.optimizador import optimizar_matricula
from modulos.matricula import confirmar_matricula, esta_confirmada
from modulos.resumen import ver_resumen
from modulos.utilidades import ANCHO


seleccionados = []

OPCIONES_MENU = [
    "1. Ver cursos disponibles",
    "2. Buscar curso",
    "3. Ver cursos con prerrequisitos",
    "4. Ver cursos ya llevados",
    "5. Seleccionar cursos",
    "6. Retirar curso de mi selección",
    "7. Ver mi selección",
    "8. Generar horario automáticamente",
    "9. Optimizar matrícula",
    "10. Confirmar/Anular matrícula",
    "11. Ver resumen de matrícula",
]


def _linea(texto="", centrar=False):
    contenido = texto.center(ANCHO) if centrar else ("  " + texto).ljust(ANCHO)
    print("║" + contenido + "║")


def mostrar_menu():
    print("╔" + "═" * ANCHO + "╗")
    _linea()
    _linea("Sistema de Matrícula Académica", centrar=True)
    _linea(f"Créditos Máximos: {CREDITOS_MAXIMOS}", centrar=True)
    print("╠" + "═" * ANCHO + "╣")
    _linea()
    for opcion in OPCIONES_MENU:
        _linea(opcion)
    _linea()
    _linea("0. Salir")
    print("╚" + "═" * ANCHO + "╝")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        print("\n" + "─" * 54)
        if opcion == "1":
            mostrar_cursos()
        elif opcion == "2":
            termino = input("Ingrese el código o nombre del curso: ").strip()
            buscar_curso(termino)
        elif opcion == "3":
            ver_curso_pre()
        elif opcion == "4":
            mostrar_cursos_llevados()
        elif opcion == "5":
            codigo = input("Ingrese el código del curso: ").strip().upper()
            seleccionar_curso(codigo, seleccionados)
        elif opcion == "6":
            codigo = input("Ingrese el código del curso a retirar: ").strip().upper()
            retirar_curso(codigo, seleccionados)
        elif opcion == "7":
            ver_seleccion(seleccionados)
        elif opcion == "8":
            generar_horario()
        elif opcion == "9":
            optimizar_matricula(seleccionados)
        elif opcion == "10":
            confirmar_matricula(seleccionados)
        elif opcion == "11":
            ver_resumen(seleccionados, esta_confirmada())
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        print("─" * 54 + "\n")

        input("Presione Enter para continuar...")
        print("\n" * 2)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nSaliendo del sistema. ¡Hasta luego!")
