# {************************************}
#    Programa:      Ejercicio 2
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Durante la planificación de un proyecto se han acordado una lista de tareas.
#                   Para cada una de estas tareas se ha asignado un orden de prioridad
#                   (cuanto menor es el número de orden, más prioridad).
# {************************************}
if __name__ == '__main__':
    tareas = [
        [6, 'Distribución'],
        [2, 'Diseño'],
        [1, 'Concepción'],
        [7, 'Mantenimiento'],
        [4, 'Producción'],
        [3, 'Planificación'],
        [5, 'Pruebas']
    ]

    print("==Tareas desordenadas==")
    for tarea in tareas:
        print(tarea[0], tarea[1])

    print(" ")
    tareas.sort()
    for tarea in tareas:
        print(tarea[0], tarea[1])
