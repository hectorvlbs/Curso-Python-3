# {************************************}
#    Programa:      Funciones recursivas.
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
# {************************************}

#  Funciones
# {************************************}
#    Función:       factorial
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         29/02/2020
# {************************************}
def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero-1)
    return numero


# {************************************}
#    Función:       cuenta atras
#    Autor:         Villalobos Valenzuela Jesús Héctor
# {************************************}
def cuenta_atras(numero):
    numero -= 1
    if (numero > 0):
        print(numero)
        cuenta_atras(numero)
    else:
        print("Se acabo el número.")


if __name__ == '__main__':
    cuenta_atras(3)
    n = 10
    m = factorial(n)
    print(m)