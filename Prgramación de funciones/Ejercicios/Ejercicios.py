# {************************************}
#    Programa:      Ejercicios de unidad
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
# {************************************

import math


#  Funciones
# {************************************}
#    Función:       Ejercicio 1 - area rectangulo
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Realizar una función llamada 'area_rectangulo(base,altura)'
#                   que devuelva el área del rectangulo a partir de una base y
#                   una altura. Calcula el área de un rectángulo de 15 de base
#                   y 10 de altura
# {************************************}
def area_rectangulo(base, altura):
    print("El área del rectangulo es de: '{} m^2'.".format(str(base * altura)))


# {************************************}
#    Función:       Ejercicio 2 - area ciruculo
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         03/02/2020
#    Descripción:   Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo
#                   a partir de un radio. Calcula el área de un círculo de 5 de radio:
# {************************************}
def area_circulo(radio):
    print("El área del circulo es de: '{}' unidades cuadraticas".format(str(math.pi * radio * radio)))


# {************************************}
#    Función:       Ejercicio 3 - relacion
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         03/02/2020
#    Descripción:   Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
#                       Si el primer número es mayor que el segundo, debe devolver 1.
#                       Si el primer número es menor que el segundo, debe devolver -1.
#                       Si ambos números son iguales, debe devolver un 0.
# {************************************}
def relacion(a, b):
    if a > b:
        print("1")
    elif a < b:
        print("-1")
    else:
        print("0")


# {************************************}
#    Función:       Ejercicio 4 - intermedio
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         03/02/2020
#    Descripción:   Realiza una función llamada intermedio(a, b) que a partir de dos números,
#                   devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:
# {************************************}
def intermedio(a, b):
    print("El punto intermedio entre le número {} y el número {} es de: {}".format(str(a), str(b), str(a + b / 2)))


# {************************************}
#    Función:       Ejercicio 5 - separar
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         03/02/2020
#    Descripción:   Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas.
#                   La primera con los números pares y la segunda con los números impares.
# {************************************}
def separar(lista):
    lista.sort()
    impares = []
    pares = []
    for index in lista:
        if index % 2 == 0:
            pares.append(index)
        else:
            impares.append(index)
    return impares, pares

if __name__ == '__main__':
    # area_rectangulo(15, 10)
    # area_circulo(12)
    # relacion(123, 2)
    # intermedio(-12, 24)
    numeros = [-12, 84, 13, 20, -33, 101, 9]
    impares, pares = separar(numeros)
    print("Lista de numeros pares {}".format(str(pares)))
    print("Lista de numeros impares {}".format(str(impares)))
