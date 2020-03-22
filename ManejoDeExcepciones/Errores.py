# {************************************}
#    Programa:      Errores
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         06/03/2020
# {************************************}
if __name__ == '__main__':
    l = []
    if len(l) > 0:
        l.pop()
    else:
        print("Vacio")

    try:
        a = "q"
        print("{} + {} = {}".format(a, 2, a * 2 / 21))
    except:
        print("Error")

    try:
        v = input("Intriduce un numero: ")
        5/v
    except Exception as e:
        print("Error -> {}".format(type(e).__name__))
