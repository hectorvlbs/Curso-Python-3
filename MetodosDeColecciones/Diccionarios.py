# {************************************}#    Programa:      Métodos de las colecciones - Diccionarios#    Autor:         Villalobos Valenzuela Jesús Héctor#    Fecha:         28 de Marzo del 2020#    Descripción:# {************************************}if __name__ == '__main__':    colores = {"Blue": "Azul", "Red": "Rojo", "Green": "Verde"}    print(colores['Blue'])    print(colores.get('Bluef', 'No se encontro ese color.'))    print(colores.keys())    print(colores.values())    print(colores.items())