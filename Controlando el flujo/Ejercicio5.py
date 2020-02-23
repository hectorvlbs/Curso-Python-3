# {************************************}
#    Programa:      Ejercicio 5
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Realizar un programa que pida al usuario
#                   un número entero del 0 al 9, y que mientras
#                   el número no sea correcto se repita el proceso.
#                   Luego debe comprobar si el número se encuentra
#                   en la lista de números y notificarlo.
# {************************************}
if __name__ == '__main__':
    numeros = [1, 4, 7, 8]
    while (True):
        print("Introduce un número entre el 0 y el 9")
        entrada = int(input())
        if (entrada >= 0 and entrada <= 9):
            if (numeros.__contains__(entrada)):
                print("El número " + str(entrada) + " se encuentra en la" \
                                                    "siguiente lista " + str(numeros))
                exit()
            else:
                print("El número " + str(entrada) + " NO se encuentra en la" \
                                                    "siguiente lista " + str(numeros))
