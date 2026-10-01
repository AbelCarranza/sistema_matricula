from data.cursos_data import CREDITOS_MAXIMOS

def ver_resumen(seleccionados):
    """Muestra un resumen completo con el total de créditos y detalle de la matrícula (Opción 9)."""
    print("\n╔════════════════════════════════════════════════════╗")
    print("║               RESUMEN DE MATRÍCULA                 ║")
    print("╚════════════════════════════════════════════════════╝")
    
    if not seleccionados:
        print("⚠️ No tienes ningún curso seleccionado en tu matrícula.")
        return

    total_creditos = 0
    
    for curso in seleccionados:
        total_creditos += curso['creditos']
        print(f"• [{curso['codigo']}] {curso['nombre']} - {curso['creditos']} créditos")
        print(f"  Horario: {curso['dia']} {curso['hora_inicio']:.2f} - {curso['hora_fin']:.2f}")
    
    print("-" * 54)
    print(f"Total de cursos seleccionados: {len(seleccionados)}")
    print(f"Total de créditos acumulados: {total_creditos} / {CREDITOS_MAXIMOS}")
    
    if total_creditos > CREDITOS_MAXIMOS:
        print("⚠️ Advertencia: Has superado el límite máximo de créditos permitidos.")
    else:
        print("Estado: Los créditos están dentro del rango permitido.")