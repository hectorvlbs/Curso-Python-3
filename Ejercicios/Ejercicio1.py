#{************************************}
#    Programa:      Ejercicio 1
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Realiza un programa que siga las siguientes instrucciones:
#                   º-> Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#                   º-> Crea un conjunto llamado administradores con los administradores Juan y Marta.
#                   º-> Borra al administrador Juan del conjunto de administradores.
#                   º-> Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
#                   º-> Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar
#                      cada usuario es administrador o no.
#{************************************}
if __name__ == '__main__':
    usuarios = {'Martha','David','Elvira','Juan','Marcos'}
    administradores = {'Juan','Martha'}

    print("Usuarios-> " + str(usuarios))
    print("Administradores-> " + str(administradores))

    print("Se removio a 'Juan' de la lista de administradores.")
    administradores.discard('Juan')
    print("Administradores-> " + str(administradores))

    print("Se añadio a 'Marcos' a la lista de administradores.")
    administradores.add('Marcos')
    print("Administradores-> " + str(administradores))

    for index in usuarios:
        print("Usuario -> " +index)

    for index in administradores:
        print("Administrador -> " +index)
