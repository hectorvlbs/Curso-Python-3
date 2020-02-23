#{************************************}
#    Programa:      Tuplas
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#{************************************}
if __name__ == '__main__':
    tupla = (100,"Hola",[1,2,3,2],True,"Hola")

    print(tupla[0])
    print(tupla.index(100))
    #print(tupla.index(1200))
    print(tupla.count(100))
    print(tupla.count("Hola"))