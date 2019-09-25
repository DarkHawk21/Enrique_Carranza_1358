# Hacer un diccionario que represente la descripción de un curso de la carrera de Ingeniería en Computación.
# @Author: Carranza Balderas Enrique
# FES Aragón UNAM - ICO
# Group: 1358

subject_ICO = {
    'asignatura': 'Estructura de datos',
    'escuela': 'UNAM',
    'facultad': 'FES Aragón',
    'carrera': 'ICO',
    'semestre': '3',
    'creditos': 8,
    'plan': '1279',
    'area': 'Programación e Ingeniería de Software',
    'caracter': 'obligatoria',
    'clave': '0190',
    'horas' : {
        'teoria': '64',
        'practica': '0'
    },
    'tipo': 'Teórica',
    'modalidad': 'curso',
    'asignaturas_indicativas': {
        'precedentes': [
            'Computadoras y Pogramación',
            'Programación Orientada a Objetos',
            'Álgebra',
            'Diseño y análisis de algoritmos',
        ],
        'subsecuentes': [
            'Diseño y análisis de algoritmos',
            'Ingeniería de software I y II',
            'Bases de datos I y II',
            'Visualización',
            'Estructuras discretas',
            'Programación de sistemas',
            'Graficación por computadora',
            'Reconocimiento de patrones',
            'Inteligencia Artificial'
        ]
    },
    'objetivos': 'El alumno resolverá problemas de almacenamiento, recuperación y ordenamiento de datos, utilizando las estructuras para representarlos y las técnicas de operación más eficientes.',
    'unidades_temáticas': {
        'unidad_1': {
            'nombre': 'Estructuras de datos elementales',
            'horas': '8',
            'temas': {
                '1.1': [
                    'Generalidades',
                    {
                        '1.1.1': 'Almacenamiento de datos',
                        '1.1.2': 'Memoria primaria',
                        '1.1.3': 'Memoria secundaria'
                    }
                ],
                '1.2': 'Representación de numeros enteros',
                '1.3': 'Representación de números reales. Estándar IEEE754',
                '1.4': 'Representación de caractéres',
                '1.5': 'Representación de arreglos',
                '1.6': 'Cardinalidad de los conjuntos de datos'
            }
        },
        'unidad_2': {
            'nombre': 'Métodos de ordenamiento',
            'horas': '12',
            'temas': {
                '2.1': 'Generalidades',
                '2.2': [
                    'Ordenamientos internos',
                    {
                        '2.2.1': 'Métodos por selección',
                        '2.2.2': 'Métodos por intercambio',
                        '2.2.3': 'Métodos por inserción',
                        '2.2.4': 'Métodos por distribución',
                        '2.2.5': 'Métodos por intercalación'
                    }
                ],
                '2.3': [
                    'Ordenamientos externos',
                    {
                        '2.3.1': 'Método por polifase',
                        '2.3.2': 'Método por cascada',
                        '2.3.3': 'Método por oscilante',
                        '2.3.4': 'Método por distribución'
                    }
                ]
            }
        }
    },
    'bibliografia': {
        'básica': [
            {
                'id': 1,
                'autor': 'JOYANES AGUILAR, LUIS',
                'titulo': 'Estructuras de datos',
                'editorial': 'McGraw-Hill',
                'ano': '2005',
                'lugar': 'México',
                'capitulos': 'todos'
            },
            {
                'id': 2,
                'autor': 'JDEITEL, DEITEL',
                'titulo': 'Estructura de datos en C y C++',
                'editorial': 'McGraw-Hill',
                'ano': '1999',
                'lugar': 'México',
                'capitulos': 'todos'
            }
        ],
        'complementaria': [
            {
                'id': 1,
                'autor': 'PAGE, E. y WILSON, L.',
                'titulo': 'Information, representation and manipulation in a computer.',
                'editorial': 'Cambridge University Press',
                'ano': '1978',
                'lugar': 'Gran Bretaña',
                'capitulos': 'todos'
            },
            {
                'id': 2,
                'autor': 'PFALTS, J.',
                'titulo': 'Computer data structures',
                'editorial': 'McGraw-Hill',
                'ano': '1977',
                'lugar': 'E.U.A.',
                'capitulos': 'todos'
            }
        ]
    },
    'sugerencias_didacticas': [
        'Exposición oral',
        'Exposición audiovisual',
        'Ejercicios dentro de clase',
        'Ejercicios fuera del aula',
        'Seminarios',
        'Lecturas obligatorias',
        'Trabajos de investigación',
        'Prácticas o taller de laboratorio',
        'Prácticas de campo'
    ],
    'evaluacion': [
        'Exámenes parciales',
        'Exámenes finales',
        'Trabajos y tarea fuera del aula',
        'Participación en clase',
        'Asistencia a prácticas'
    ],
    'activa': True
}

print(subject_ICO)

print('\n\nDeveloped by: DarkHawk21')
