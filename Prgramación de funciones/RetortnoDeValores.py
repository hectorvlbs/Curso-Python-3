# {************************************}
#    Programa:      Retornando valores
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Entradas de datos.
# {************************************}

#  Funciones
#{************************************}
#    Función:       devuelve arreglo
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         26/02/2020
#{************************************}
def devuelve_arreglo():
    return [1,2,3,4,5]

#{************************************}
#    Función:       devuelve cadena de texto
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         26/02/2020
#{************************************}
def devuelve_cadena_de_texto():
    return "Soy una cadena de texto."

if __name__ == '__main__':
    print(devuelve_cadena_de_texto())
    print(devuelve_arreglo())