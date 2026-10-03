"""Compara fuerza bruta, algoritmo voraz y backtracking con conjuntos de cursos de distinto tamaño.

    python pruebas/benchmark.py

Genera cursos sintéticos (semilla fija, resultados reproducibles) y muestra, por algoritmo, el
tiempo de ejecución, las combinaciones evaluadas y si alcanzó el puntaje óptimo.
Sirve de base para la sección 4.1 (Análisis empírico) del informe.
"""
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modulos.optimizador import (optimizar_backtracking, optimizar_fuerza_bruta,
                                 optimizar_voraz, puntaje)

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
TAMANOS = [8, 10, 12, 14, 16, 18, 20, 24, 28]
LIMITE_FUERZA_BRUTA = 18     # 2^n crece demasiado: por encima de este tamaño no se ejecuta
REPETICIONES = 3             # se promedia el tiempo de cada algoritmo


def generar_cursos(n, semilla=2026):
    azar = random.Random(semilla + n)
    cursos = []
    for i in range(n):
        inicio = azar.choice([8, 10, 12, 14, 16])
        cursos.append({"codigo": f"C{i:02d}", "nombre": f"Curso {i}", "creditos": azar.randint(2, 4),
                       "prerrequisito": "Ninguno", "dia": azar.choice(DIAS),
                       "hora_inicio": float(inicio), "hora_fin": float(inicio + 2)})
    return cursos


def medir(algoritmo, cursos):
    inicio = time.perf_counter()
    for _ in range(REPETICIONES):
        resultado, stats = algoritmo(cursos)
    return resultado, stats, (time.perf_counter() - inicio) / REPETICIONES * 1000


def main():
    print(f"{'n':>3} | {'Algoritmo':<13} | {'Tiempo (ms)':>12} | {'Evaluadas':>10} | "
          f"{'Cursos':>6} | {'Créd.':>5} | Óptimo")
    print("-" * 78)
    for n in TAMANOS:
        cursos = generar_cursos(n)
        # Referencia del óptimo: fuerza bruta cuando es viable; si no, backtracking.
        algoritmo_referencia = optimizar_fuerza_bruta if n <= LIMITE_FUERZA_BRUTA else optimizar_backtracking
        optimo = puntaje(algoritmo_referencia(cursos)[0])

        corridas = [("Fuerza bruta", optimizar_fuerza_bruta), ("Voraz", optimizar_voraz),
                    ("Backtracking", optimizar_backtracking)]
        for nombre, algoritmo in corridas:
            if algoritmo is optimizar_fuerza_bruta and n > LIMITE_FUERZA_BRUTA:
                print(f"{n:>3} | {nombre:<13} | {'(omitido)':>12} | {2 ** n:>10} | {'-':>6} | {'-':>5} | -")
                continue
            resultado, stats, ms = medir(algoritmo, cursos)
            valor = puntaje(resultado)
            print(f"{n:>3} | {nombre:<13} | {ms:>12.2f} | {stats['evaluadas']:>10} | "
                  f"{valor[0]:>6} | {valor[1]:>5} | {'sí' if valor == optimo else 'no'}")
        print("-" * 78)


if __name__ == "__main__":
    main()
