# {************************************}
#    Programa:      Realizar un programa sume todos los números
#                   enteros pares desde el 0 hasta el 100
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
# {************************************}
if __name__ == '__main__':
    Arreglo1 = []
    Arreglo2 = []
    n = 100
    suma = 0

    for index in range(n):
        Arreglo1.append(index)

    for index in range(len(Arreglo1)):
        if (Arreglo1[index] % 2 == 0):
            Arreglo2.append(index)

    for index in range(len(Arreglo2)):
        suma = suma + Arreglo2[index]

    print(suma)