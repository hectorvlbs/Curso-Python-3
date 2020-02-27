# {************************************}
#    Programa:      Definición de funciones
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Entradas de datos.
# {************************************}



#  Funciones
#{************************************}
#    Función:       saludar
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         26/02/2020
#{************************************}
def saludar():
    print("Hola desde la función Saludar() ...")

#  Funciones
#{************************************}
#    Función:       dibujar tabla del 5
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         26/02/2020
#{************************************}
def dibujar_tabla_del_5():
    for index in range(10):
        print("{} x {} = {}".format(index+1,5,(index+1)*5))





if __name__ == '__main__':
    saludar()
    dibujar_tabla_del_5()