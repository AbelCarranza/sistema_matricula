# Ver, buscar y consultar cursos

import unicodedata

from data.cursos_data import cursos, cursos_llevados
from modulos.utilidades import imprimir_curso, imprimir_titulo
from modulos.validaciones import obtener_curso


def _normalizar(texto):
    """Minúsculas y sin tildes, para que 'matematica' encuentre 'Matemática'."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")


def mostrar_cursos():
    imprimir_titulo("CURSOS DISPONIBLES")
    print()

    for curso in cursos:
        imprimir_curso(curso)
        if curso["codigo"] in cursos_llevados:
            print("Estado: Ya llevado")
        print("-" * 40)


def mostrar_cursos_llevados():
    imprimir_titulo("CURSOS YA LLEVADOS")
    print()

    if not cursos_llevados:
        print("Aún no tiene cursos aprobados registrados.")
        return

    for codigo in cursos_llevados:
        curso = obtener_curso(codigo)
        if curso is None:
            continue
        print(f"Código: {curso['codigo']}")
        print(f"Curso: {curso['nombre']}")
        print(f"Créditos: {curso['creditos']}")
        print("-" * 40)


def buscar_curso(termino):
    """Busca por código o por parte del nombre. Devuelve la lista de cursos encontrados."""
    buscado = _normalizar(termino.strip())

    if not buscado:
        print("Debe ingresar un código o un nombre de curso.")
        return []

    encontrados = [
        curso for curso in cursos
        if buscado in _normalizar(curso["codigo"]) or buscado in _normalizar(curso["nombre"])
    ]

    if not encontrados:
        print("Curso no existe")
        return []

    print(f"\nCursos encontrados: {len(encontrados)}")
    for curso in encontrados:
        print()
        imprimir_curso(curso)
    return encontrados


def ver_curso_pre():
    con_prerrequisito = [c for c in cursos if c["prerrequisito"] != "Ninguno"]

    imprimir_titulo("CURSOS CON PRERREQUISITOS")
    if not con_prerrequisito:
        print("No hay cursos con prerrequisitos.")
        return

    for curso in con_prerrequisito:
        print()
        imprimir_curso(curso)
