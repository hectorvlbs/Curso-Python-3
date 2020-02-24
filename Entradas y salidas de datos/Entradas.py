# {************************************}
#    Programa:      Entradas
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Entradas de datos.
# {************************************}
if __name__ == '__main__':
    valores = []
    print("Introduce 3 valores")
    for x in range(3):
        valores.append(input("Introduce el numero "+str(x+1)))

    print(valores)