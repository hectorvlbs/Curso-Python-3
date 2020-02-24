# {************************************}
#    Programa:      Ejercicio 2
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Descripción:   Durante el desarrollo de un pequeño videojuego se te encarga configurar y
#                   balancear cada clase de personaje jugable. Partiendo que la estadística base es 2,
#                   debes cumplir las siguientes condiciones:
#                   -> El caballero tiene el doble de vida y defensa que un guerrero.
#                   -> El guerrero tiene el doble de ataque y alcance que un caballero.
#                   -> El arquero tiene la misma vida y ataque que un guerrero,
#                      pero la mitad de su defensa y el doble de su alcance.
#                   -> Muestra como quedan las propiedades de los tres personajes.
# {************************************}
if __name__ == '__main__':
    caballero = {'Vida': 4, 'Defensa': 4, 'Ataque': 2, 'Alcance': 2}
    guerrero = {'Vida': 2, 'Defensa': 2, 'Ataque': 4, 'Alcance': 4}
    arquero = {'Vida': 2, 'Defensa': 1, 'Ataque': 4, 'Alcance': 8}

    print("Propiedades del caballero:")
    for k,v in caballero.items():
        print("-> " + k,v)

    print("Propiedades del guerrero:")
    for k, v in guerrero.items():
        print("-> " + k, v)

    print("Propiedades del arquero:")
    for k, v in arquero.items():
        print("-> " + k, v)

