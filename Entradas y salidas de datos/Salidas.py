# {************************************}
#    Programa:      Salidas
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Entradas de datos.
# {************************************}
if __name__ == '__main__':
    v = "otro texto"
    n = 10
    c = "Un texto {} y un número {}".format(v,n)
    print(c)

    print("{:>50}".format("HOLA MUNDO"))

    # Formateo de números enteros
    print("{:4d}".format(10))
    print("{:4d}".format(100))
    print("{:4d}".format(1000))
    print(" ")
    print("{:04d}".format(10))
    print("{:04d}".format(100))
    print("{:04d}".format(1000))

    # Formateo de números decimales
    print("{:7.3f}".format(3.14))
    print("{:7.3f}".format(123.12))
    #print("{:04d}".format(100))
    #print("{:04d}".format(1000))