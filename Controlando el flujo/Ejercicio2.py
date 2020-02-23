# {************************************}
#    Programa:      Realizar un programa que lea un número impar
#                   por teclado.
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Realizar un programa que lea un número impar
#                   por teclado. Si el usuario no introduce un número
#                   impar, debe repetirse el proceso hasta que lo
#                   introduzca correctamente.
# {************************************}
if __name__ == '__main__':

    repeticion = False

    while (repeticion != True):
        print("Introduce un número:")
        entrada = float(input())

        if (entrada % 2):
            print(" -> Tu número es impar, bye.")
            repeticion = True
        else:
            print(" -> Tu número es par.")
            print(" -> Favor de introducir de nuevo un número.")

    if (repeticion == True):
        exit()

