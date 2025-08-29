# Lista de estudiantes representados como tuplas
estudiantes = [
    ("Luis", 22, "Economía"),
    ("Ana", 21, "Ingeniería"),
    ("Carlos", 23, "Economía")
]


print("Nombre del segundo estudiante:", estudiantes[1][0])
"""Cambio de nombre por medio de indice"""


nuevo_estudiante = (estudiantes[0][0], estudiantes[0][1], "Ingeniería de Datos")
estudiantes[0] = nuevo_estudiante
print("Estudiante actualizado:", estudiantes[0])
"""Cambia la carrera del primer estudiante """


contador = sum(1 for estudiante in estudiantes if estudiante[2] == "Economía")
print("Cantidad de estudiantes en Economía:", contador)
"""Cuenta cuantos estudian economia"""
