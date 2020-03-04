# {************************************}
#    Programa:      Enviando valores
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Entradas de datos.
# {************************************}

#  Funciones
# {************************************}
#    Función:       suma
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         26/02/2020
#    Desprición:    Está función resive dos números de entrada y lo suma.
# {************************************}
def suma(a, b):
    print("Suma de {} + {} =  {}".format(a, b, a + b))


# {************************************}
#    Función:       resta
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         26/02/2020
#    Desprición:    Está función resive dos números de entrada y los resta.
# {************************************}
def resta(a, b):
    print("Resta de {} - {} =  {}".format(a, b, a - b))


# {************************************}
#    Función:       doblar valor
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         26/02/2020
#    Desprición:    Está función resive un número y dobla su valor.
# {************************************}
def doblar_valor(numero):
    return numero * 2


def indeterminadors_posicion(*args):
    print(args)


def indeterminados_nombre(**kwargs):
    for k,v in kwargs.items():
        print("Key '{}', value '{}'.".format(k,v))


if __name__ == '__main__':
    # suma(1, 2)
    # resta(123.22, 4)
    # n = 10
    # n = doblar_valor(n)
    # print(n)
    # indeterminadors_posicion(123, "HOlA", [1, 2, 3])
    indeterminados_nombre(n=1, c="HOLA", l=[12, 3, 2])
