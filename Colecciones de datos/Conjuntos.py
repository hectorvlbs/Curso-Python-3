#{************************************}
#    Programa:      Conjuntos
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#{************************************}
if __name__ == '__main__':
    conjunto = set()
    conjunto = {1,2,3,4,1,2,3,4,1,2,3,4}
    conjunto.add("H")
    conjunto.add("A")
    print(conjunto)

    print('Jesus' in conjunto)

    lista = list(conjunto)
    print(lista)