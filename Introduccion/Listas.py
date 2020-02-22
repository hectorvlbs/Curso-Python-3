#{************************************}
#    Programa:      Introducción a la programación con python3,
#                   manejando listas.
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         21/02/2020
#{************************************}

if __name__ == '__main__':
    numeros = [1,2,3,4,5,6,7,8,9,10]
    datos = [1,"Una cadena",True,False,2,"Otra cadena",1.223]

    print(datos[1])
    print(datos[:2])

    datos.append(2)
    datos.append(True)
    print(datos)

    lista = [numeros,datos]
    print(lista[1][2])