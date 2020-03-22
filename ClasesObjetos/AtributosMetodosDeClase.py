# {************************************}
#    Programa:      Atributos y métodos de clase
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         20/Marzo/2020
#    Descripción:   Programación Orientada a Objetos
# {************************************}
class Galleta():
    chocolate = False
    def __init__(self, sabor):
        self.sabor = sabor
        print("Se creo una galleto de sabor {}".format(self.sabor))

    def Chocolatear(self):
        self.chocolate = True

    def Tiene_Chocolate(self):
        if  self.chocolate == True:
            return "Tengo chocolate uwu"
        else:
            return "No tengo chocolate unu"

if __name__ == '__main__':
    galleta = Galleta("Oreo")

    galleta.Chocolatear()

    print(galleta.Tiene_Chocolate())