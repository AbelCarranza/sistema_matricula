# Optimizar matrícula
#
# CRITERIO DE OPTIMIZACIÓN (verificable). Entre todas las combinaciones válidas
# (prerrequisitos cumplidos, créditos <= máximo y sin cruces de horario) se prefiere:
#   1) la que tenga MÁS CURSOS;
#   2) a igualdad de cursos, la de MÁS CRÉDITOS;
#   3) a igualdad de créditos, la que use MENOS DÍAS de clase.
#
# Algoritmo principal: búsqueda con retroceso (backtracking) con poda. Se incluyen también
# fuerza bruta y un algoritmo voraz para poder compararlos (ver pruebas/benchmark.py).
# Cada algoritmo devuelve (cursos_elegidos, estadisticas).

from itertools import combinations

from data.cursos_data import CREDITOS_MAXIMOS
from modulos.matricula import esta_confirmada
from modulos.utilidades import clave_horario, formato_horario, imprimir_titulo, pedir_si_no
from modulos.validaciones import hay_cruce, obtener_cursos_disponibles, total_creditos


def puntaje(combinacion):
    """Tupla comparable según el criterio: mayor es mejor."""
    dias = len({curso["dia"] for curso in combinacion})
    return (len(combinacion), total_creditos(combinacion), -dias)


def es_valida(combinacion, limite=CREDITOS_MAXIMOS):
    """Comprueba límite de créditos y ausencia de cruces."""
    if total_creditos(combinacion) > limite:
        return False
    for i, curso in enumerate(combinacion):
        for otro in combinacion[i + 1:]:
            if hay_cruce(curso, otro):
                return False
    return True


def optimizar_backtracking(candidatos, limite=CREDITOS_MAXIMOS):
    """Búsqueda con retroceso: decide curso por curso (incluir / no incluir) y poda las ramas
    que incumplen una restricción o que ya no pueden superar a la mejor solución encontrada."""
    orden = sorted(candidatos, key=clave_horario)
    n = len(orden)
    minimo_creditos = min((c["creditos"] for c in orden), default=0)

    mejor = {"cursos": [], "puntaje": puntaje([])}
    estadisticas = {"evaluadas": 0, "podas": 0}

    def explorar(i, actual, creditos):
        estadisticas["evaluadas"] += 1

        # Cota: máximo de cursos que aún podrían agregarse (por cursos restantes y por créditos).
        restantes = n - i
        if minimo_creditos > 0:
            restantes = min(restantes, (limite - creditos) // minimo_creditos)
        if len(actual) + restantes < len(mejor["cursos"]):
            estadisticas["podas"] += 1
            return

        if i == n:
            valor = puntaje(actual)
            if valor > mejor["puntaje"]:
                mejor["cursos"] = list(actual)
                mejor["puntaje"] = valor
            return

        curso = orden[i]

        # Rama 1: incluir el curso (solo si respeta créditos y horario).
        if creditos + curso["creditos"] <= limite and not any(hay_cruce(curso, c) for c in actual):
            actual.append(curso)
            explorar(i + 1, actual, creditos + curso["creditos"])
            actual.pop()

        # Rama 2: no incluirlo.
        explorar(i + 1, actual, creditos)

    explorar(0, [], 0)
    return mejor["cursos"], estadisticas


def optimizar_fuerza_bruta(candidatos, limite=CREDITOS_MAXIMOS):
    """Genera y evalúa todos los subconjuntos posibles (2^n)."""
    orden = sorted(candidatos, key=clave_horario)
    mejor, mejor_valor = [], puntaje([])
    evaluadas = 0

    for tamano in range(len(orden) + 1):
        for combinacion in combinations(orden, tamano):
            evaluadas += 1
            if es_valida(combinacion, limite):
                valor = puntaje(combinacion)
                if valor > mejor_valor:
                    mejor, mejor_valor = list(combinacion), valor

    return mejor, {"evaluadas": evaluadas, "podas": 0}


def optimizar_voraz(candidatos, limite=CREDITOS_MAXIMOS):
    """Voraz: toma primero los cursos de menos créditos y conserva los que aún caben."""
    orden = sorted(candidatos, key=lambda c: (c["creditos"], clave_horario(c)))
    elegidos, creditos = [], 0

    for curso in orden:
        if creditos + curso["creditos"] > limite:
            continue
        if any(hay_cruce(curso, otro) for otro in elegidos):
            continue
        elegidos.append(curso)
        creditos += curso["creditos"]

    return elegidos, {"evaluadas": len(orden), "podas": 0}


def optimizar_matricula(seleccionados):
    """Busca la mejor combinación entre los cursos que el estudiante puede llevar y,
    si mejora su selección actual, ofrece reemplazarla."""
    imprimir_titulo("OPTIMIZAR MATRÍCULA")

    if esta_confirmada():
        print("Su matrícula ya fue confirmada. Anule la confirmación para poder optimizarla.")
        return None

    candidatos = obtener_cursos_disponibles()
    if not candidatos:
        print("No hay cursos disponibles para optimizar.")
        return None

    propuesta, stats = optimizar_backtracking(candidatos)

    if not propuesta:
        print("No existe ninguna combinación válida con las restricciones actuales.")
        return None

    print("Propuesta óptima:\n")
    for curso in sorted(propuesta, key=clave_horario):
        print(f"  • [{curso['codigo']}] {curso['nombre']} - {curso['creditos']} créditos | "
              f"{formato_horario(curso)}")

    dias = len({curso["dia"] for curso in propuesta})
    print(f"\nCursos: {len(propuesta)} | Créditos: {total_creditos(propuesta)} / {CREDITOS_MAXIMOS} "
          f"| Días de clase: {dias}")

    if seleccionados and puntaje(seleccionados) >= puntaje(propuesta):
        print("\nSu selección actual ya es la mejor combinación posible. No se realizaron cambios.")
        return propuesta

    if seleccionados:
        print(f"\nSu selección actual: {len(seleccionados)} cursos, "
              f"{total_creditos(seleccionados)} créditos.")
        pregunta = "¿Desea reemplazar su selección por esta propuesta? (s/n): "
    else:
        pregunta = "¿Desea cargar esta propuesta como su selección? (s/n): "

    if pedir_si_no("\n" + pregunta):
        seleccionados[:] = sorted(propuesta, key=clave_horario)
        print("Selección actualizada correctamente.")
    else:
        print("Se mantuvo su selección actual.")

    return propuesta
