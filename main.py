from data.cursos_data import CREDITOS_MAXIMOS
from modulos.consulta import mostrar_cursos, buscar_curso_code,ver_curso_pre


def mostrar_menu():
    print("╔════════════════════════════════════════════════════╗")
    print("║                                                    ║")
    print("║           Sistema de Matrícula Académica           ║")
    print(f"║               Créditos Máximos: {CREDITOS_MAXIMOS}                 ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║                                                    ║")
    print("║  1. Ver cursos disponibles                         ║")
    print("║  2. Buscar curso                                   ║")
    print("║  3. Ver cursos con prerrequisitos                  ║")
    print("║  4. Seleccionar cursos                             ║")
    print("║  5. Ver mi selección                               ║")
    print("║  6. Generar horario                                ║")
    print("║  7. Optimizar matrícula                            ║")
    print("║  8. Confirmar matrícula                            ║")
    print("║  9. Ver resumen de matrícula                       ║")
    print("║                                                    ║")
    print("║  0. Salir                                          ║")
    print("╚════════════════════════════════════════════════════╝")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        print("\n" + "─" * 54)
        if opcion == "1":
            mostrar_cursos()
        elif opcion == "2":
            codigo = input("Ingrese el codigo del curso: ").strip().upper()
            buscar_curso_code(codigo)
        elif opcion == "3":
            ver_curso_pre()
        elif opcion == "4":
            seleccionar_curso()
        elif opcion == "5":
            ver_seleccion()
        elif opcion == "6":
            generar_horario()
        elif opcion == "7":
            optimizar_matricula()
        elif opcion == "8":
            confirmar_matricula()
        elif opcion == "9":
            ver_resumen()
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        print("─" * 54 + "\n")

        input("Presione Enter para continuar...")
        print("\n" * 2)


if __name__ == "__main__":
    main()