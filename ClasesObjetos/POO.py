# {************************************}
#    Programa:      POO
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         20/Marzo/2020
#    Descripción:   Programación Orientada a Objetos
# {************************************}
class cliente:
    def __init__(self, dni, nombres, apellidos):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos

    def __str__(self):
        return 'Nombres: {}\n' \
               'Apellidos: {}\n' \
               'DNI: {}'.format(self.nombres, self.apellidos, self.dni)


class empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def __str__(self):
        clientes =""
        for index in self.clientes:
            clientes = clientes + "Nombres: {}, apellidos: {}".format(index.nombres,index.apellidos) + "\n"
        return clientes

    def mostrar_cliente(self, dni=None):
        for index in self.clientes:
            if index.dni == dni:
                print(index)
                return
        print("Cliente no encontrado.")

    def borrar_cliente(self, dni=None):
        for index, c in enumerate(self.clientes):
            if c.dni == dni:
                del (self.clientes[index])
                print(str(c) + "\n ---- Borrado. ----")
                return
        print("Cliente no encontrado")


if __name__ == '__main__':
    Cliente1 = cliente(1, "Jesús Héctor", "Villalobos Valenzuela")
    Cliente2 = cliente(2, "Juan Alberto", "Lopez Lopez")

    Empresa = empresa(clientes=[Cliente1,Cliente2])
    #print(Empresa)
    Empresa.mostrar_cliente(0)
    Empresa.borrar_cliente(1)
