# {************************************}
#    Programa:      Métodos especiales de clase
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         20/Marzo/2020
#    Descripción:   Programación Orientada a Objetos
# {************************************}
class Pelicula:
    # Constructor de clase
    def __init__(self, Titulo, Duracion, Lanzamiento):
        self.Titulo = Titulo
        self.Duracion = Duracion
        self.Lanzamiento = Lanzamiento
        print("Se ha creado la pelicula {}".format(self.Titulo))

    def __str__(self):
        return '"{}" lanzada en el año {} con una duración de {} minutos.'.format(self.Titulo, self.Lanzamiento,
                                                                                self.Duracion)


if __name__ == '__main__':
    pelicula1 = Pelicula("El padrino", 172, 1972)
    pelicula2 = Pelicula("El Señor de los Anillos: el retorno del Rey", 201, 2003)

    print(pelicula1)
    print(pelicula2)
