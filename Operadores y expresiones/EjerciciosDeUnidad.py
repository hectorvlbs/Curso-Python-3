#    Programa:  Introducción a la programación con python3,
#               ejercicios de unidad.
#    Autor:     Villalobos Valenzuela Jesús Héctor
#    Fecha:     22/02/2020
#{************************************}


# Funciones
# {************************************}
#    Función:       Ejercicio 1.
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         22/02/2020
#    Descripción:   Realizar un programa que lea 2 números por teclado
#                   y determine los siguientes aspectos (mostrar True o False):
#                   1) Si los dos números son iguales.
#                   2) Si los dos números son diferentes.
#                   3) Si el primero es mayor que el segundo.
#                   4) Si el segundo es mayor o igual que el primero.
# {************************************}
def Ejercicio1():
    print("Ingrese el primer número...")
    n1 = float(input())
    print("Ingrese el segundo número...")
    n2 = float(input())

    if  (n1 == n2):
        print("Los dos números son iguales.")
    elif (n1 != n2):
        if (n1 > n2):
            print("Los números son diferentes y el número: "
                  +str(n1)+ " es mayor que: " +str(n2))
        elif (n1 < n2):
            print("Los números son diferentes y el número: "
                  +str(n1)+ " es menor que: " + str(n2))
    else:
        print("Los datos son erroneos.")

# {************************************}
#    Función:       Ejercicio 2.
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         22/02/2020
#    Descripción:   Utilizando operadores lógicos, determina si una cadena de texto introducida
#                   por el usuario tiene una longitud mayor o igual que 3 y a su vez
#                   es menor que 10.
# {************************************}
def Ejercicio2():
    texto = input("Introduce una línea de texto\n")
    longitud = len(texto)

    if  (longitud >= 3 and longitud < 10):
        print("El texto introducido tiene una longitud mayor o igual que 3 y a su vez"
                   "es menor que 10.")
    else:
        print("El texto introducido NO tiene una longitud mayor o igual que 3 y a su vez"
              "es menor que 10.")

if __name__ == '__main__':
    #Ejercicio1()
    Ejercicio2()