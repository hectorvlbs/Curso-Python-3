# {************************************}
#    Programa:      Diccionarios
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
# {************************************}
if __name__ == '__main__':
    colores = {'Amarillo': 'Yellow', 'Azúl': 'Blue', 'Negro': 'Black'}

    print(colores)
    # print(type(hash))
    print(colores['Amarillo'])
    print(colores['Azúl'])
    print(colores['Negro'])

    numeros = {1: 'Uno', 2: 'Dos', 3: 'Tres'}
    print(numeros)
    numeros[1] = 'UNO'
    print(numeros)
    del (numeros[3])
    print(numeros)

    edades = {'Hector': 20, 'Juan': 12, 'Maria': 20}
    print(edades)
    edades['Hector'] += 10
    print(edades)

    for keys in edades:
        print(" ->  " + str(edades[keys]))

    for keys, values in edades.items():
        print(keys, values)

    personajes = []
    personaje = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Angel'}
    personajes.append(personaje)
    # print(personajes)
    personaje = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo'}
    personajes.append(personaje)

    for p in personajes:
        print("Nombre del personaje: " +p['Nombre']+" "
              "Clase del pesonaje: " +p['Clase']+" "
              "Raza del personaje: " +p['Raza']+"\n")

