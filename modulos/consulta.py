# Opciones 1, 2 y 3 (Ver, buscar y ver detalles de cursos)

from data.cursos_data import cursos

def mostrar_cursos():
    print("\n========== CURSOS DISPONIBLES ==========\n")

    for curso in cursos:
        print(f"Código: {curso['codigo']}")
        print(f"Curso: {curso['nombre']}")
        print(f"Créditos: {curso['creditos']}")
        print(f"Prerrequisito: {curso['prerrequisito']}")
        print(f"Horario:         {curso['dia']} {curso['hora_inicio']:.2f} - {curso['hora_fin']:.2f}")
        print("-" * 40)



