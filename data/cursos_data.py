CREDITOS_MAXIMOS = 16

cursos_llevados = [
    "PROG101",
    "MAT101"
]

cursos = [
    {
        "codigo": "ALG101",
        "nombre": "Análisis de Algoritmos",
        "creditos": 3,
        "prerrequisito": "Ninguno",
        "dia": "Lunes",
        "hora_inicio": 8.00,
        "hora_fin": 10.00
    },
    {
        "codigo": "BD101",
        "nombre": "Base de Datos",
        "creditos": 3,
        "prerrequisito": "PROG101",
        "dia": "Martes",
        "hora_inicio": 10.00,
        "hora_fin": 12.00
    },
    {
        "codigo": "PROG101",
        "nombre": "Programación I",
        "creditos": 4,
        "prerrequisito": "Ninguno",
        "dia": "Lunes",
        "hora_inicio": 10.00,
        "hora_fin": 12.00
    },
    {
        "codigo": "MAT101",
        "nombre": "Matemática I",
        "creditos": 4,
        "prerrequisito": "Ninguno",
        "dia": "Miércoles",
        "hora_inicio": 8.00,
        "hora_fin": 10.00
    },
    {
        "codigo": "SO101",
        "nombre": "Sistemas Operativos",
        "creditos": 3,
        "prerrequisito": "PROG101",
        "dia": "Jueves",
        "hora_inicio": 8.00,
        "hora_fin": 10.00
    },
    {
        "codigo": "PROG201",
        "nombre": "Programación II",
        "creditos": 4,
        "prerrequisito": "PROG101",
        "dia": "Martes",
        "hora_inicio": 8.00,
        "hora_fin": 10.00
    },
    {
        "codigo": "BD201",
        "nombre": "Base de Datos II",
        "creditos": 3,
        "prerrequisito": "BD101",
        "dia": "Miércoles",
        "hora_inicio": 10.00,
        "hora_fin": 12.00
    },
    {
        "codigo": "RED101",
        "nombre": "Redes de Computadoras",
        "creditos": 3,
        "prerrequisito": "SO101",
        "dia": "Jueves",
        "hora_inicio": 10.00,
        "hora_fin": 12.00
    },
    {
        "codigo": "IA101",
        "nombre": "Introducción a la Inteligencia Artificial",
        "creditos": 3,
        "prerrequisito": "ALG101",
        "dia": "Viernes",
        "hora_inicio": 8.00,
        "hora_fin": 10.00
    }
]