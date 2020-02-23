# {************************************}
#    Programa:      Programa que lee dos números y permita elegir
#                   entre 3 opciones del menú.
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         22/02/2020
#    Descripción:   Opciones del menú:
#                   1) Mostrar una suma de los dos números.
#                   2) Mostrar una resta de los dos números.
#                   3) Mostrar una multiplicación de los dos números.
#                   4) En caso de no introducir una opción valida,
#                      el programa informara que es incorrecta.
# {************************************}
if __name__ == '__main__':

    menu = "1) Mostrar una suma de los dos números.\n" \
           "2) Mostrar una resta de los dos números.\n" \
           "3) Mostrar una multiplicación de los dos números."

    print("Introduce un número:")
    numero1 = float(input())
    print("Introduce un número:")
    numero2 = float(input())

    print(menu)
    seleccion = int(input())

    if (seleccion == 1):
        suma = numero1 + numero2
        print("La suma de los números introducidos es de: " + str(suma))
    elif (seleccion == 2):
        resta = numero1 - numero1
        print("La resta de los números introducidos es de: " + str(resta))
    elif (seleccion == 3):
        multiplicacion = numero1 * numero2
        print("La multiplicación de los números introducidos es de: " + str(multiplicacion))
    else:
        print("Opción invalida.")
