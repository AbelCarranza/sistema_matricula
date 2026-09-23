# Opciones 1, 2 y 3 (Ver, buscar y ver detalles de cursos)

from data.cursos_data import cursos

def mostrar_cursos():
    print("\n========== CURSOS DISPONIBLES ==========\n")

    for curso in cursos:
        print(f"Código: {curso['codigo']}")
        print(f"Curso: {curso['nombre']}")
        print(f"Créditos: {curso['creditos']}")
        print("-" * 40)



def buscar_curso_code(codigo):

    for curso in cursos:
        if curso["codigo"] == codigo:
            print("\nCurso encontrado")
            print(f"Código: {curso['codigo']}")
            print(f"Curso: {curso['nombre']}")
            print(f"Créditos: {curso['creditos']}")           
            print(f"Prerrequisito: {curso['prerrequisito']}")
            print(f"Horario:         {curso['dia']} {curso['hora_inicio']:.2f} - {curso['hora_fin']:.2f}")
            return
        

    print("Curso no existe")


def seleccionar_curso(codigo, seleccionados):

    for curso in cursos:

        if curso["codigo"] == codigo:

            if curso in seleccionados:
                print("El curso ya está seleccionado")
                return

            seleccionados.append(curso)
            print("Curso seleccionado correctamente")
            return

    print("El curso no existe")
def ver_curso_pre():
    for curso in cursos:
        if curso["prerrequisito"] != "Ninguno":
            print("\nCursos con prerrequisitos")
            print(f"Código: {curso['codigo']}")
            print(f"Curso: {curso['nombre']}")
            print(f"Créditos: {curso['creditos']}")           
            print(f"Prerrequisito: {curso['prerrequisito']}")
            print(f"Horario:         {curso['dia']} {curso['hora_inicio']:.2f} - {curso['hora_fin']:.2f}")
