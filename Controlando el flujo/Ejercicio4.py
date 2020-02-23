# {************************************}
#    Programa:      Ejercicio 4
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Realiza un programa que pida al usuario
#                   cuantos números quiere introducir.
#                   Luego lee todos los números y relizar
#                   una media aritmética.
# {************************************}
if __name__ == '__main__':
    cantidad = 0
    suma = 0
    media = 0
    numeros = []

    print("¿Cuántos números va a introducir?")
    cantidad = int(input())

    for index in range(cantidad):
        print("Dame el número " +str(index+1))
        numeros.append(int(input()))

    suma = sum(numeros)
    media = suma/len(numeros)

    print("Valor de la media aritmética de los siguietes números:\n" +str(numeros) )
    print("Es de: " +str(media))
