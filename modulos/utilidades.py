# Funciones auxiliares de presentación y ordenamiento compartidas por los módulos

ORDEN_DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ANCHO = 52


def clave_horario(curso):
    """Clave de ordenamiento: día de la semana y, luego, hora de inicio."""
    dia = curso["dia"]
    posicion = ORDEN_DIAS.index(dia) if dia in ORDEN_DIAS else len(ORDEN_DIAS)
    return (posicion, curso["hora_inicio"])


def formato_horario(curso):
    return f"{curso['dia']} {curso['hora_inicio']:.2f} - {curso['hora_fin']:.2f}"


def imprimir_titulo(titulo, ancho=ANCHO):
    print("\n╔" + "═" * ancho + "╗")
    print("║" + titulo.center(ancho) + "║")
    print("╚" + "═" * ancho + "╝")


def imprimir_curso(curso, prefijo=""):
    print(f"{prefijo}Código: {curso['codigo']}")
    print(f"{prefijo}Curso: {curso['nombre']}")
    print(f"{prefijo}Créditos: {curso['creditos']}")
    print(f"{prefijo}Prerrequisito: {curso['prerrequisito']}")
    print(f"{prefijo}Horario: {formato_horario(curso)}")


def pedir_si_no(mensaje):
    """Pregunta de confirmación. Repite hasta recibir 's' o 'n'."""
    while True:
        try:
            respuesta = input(mensaje).strip().lower()
        except EOFError:
            return False
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Responda 's' (sí) o 'n' (no).")
