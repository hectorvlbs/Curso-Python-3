# {************************************}
#    Programa:      Ejercicio
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         24/Marzo/2020
#    Descripción:   Programación Orientada a Objetos
# {************************************}
import math


class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "P({},{})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante.".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante.".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante.".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante.".format(self))

    def vector(self, x, y):
        v = Punto(self.x - x, self.y - y)
        print("El vector resultando entre {} y P({},{}) es V({},{})".format(self, x, y, v.x, v.y))

    def distancia(self, Punto):
        d = math.sqrt(((Punto.x - self.x) ** 2) + ((Punto.y - self.y) ** 2))
        print("La distancia entre los puntos {} y {} es de {}".format(self, Punto, d))


class Rectangulo:
    def __init__(self, Pi=Punto(), Pf=Punto()):
        self.Pi = Pi
        self.Pf = Pf
        self.Base = abs(self.Pf.x - self.Pi.x)
        self.Altura = abs(self.Pf.y - self.Pi.y)
        self.Area = self.Base * self.Altura

    def base(self):
        print("La base del rectangulo es de {}".format(self.Base))

    def altura(self):
        print("La altura del rectangulo es de {}".format(self.Altura))

    def area(self):
        print("El área del rectangulo es de {} unidades cuadradas".format(self.Area))


if __name__ == '__main__':
    p1 = Punto(2, 3)
    p2 = Punto(5, 5)

    p1.cuadrante()

    p1.vector(12, -12)

    p1.distancia(p2)

    r = Rectangulo(p1, p2)
    r.base()
    r.altura()
    r.area()
    # print(p2)
