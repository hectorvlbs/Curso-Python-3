from _collections import deque  # <- Importación para las colas
# {************************************}
#    Programa:      Pilas y colas
#    Autor:         Villalobos Valenzuela Jesús Héctor
#    Fecha:         23/02/2020
#    Notas:         Python no cuenta con pilas y colas como Java, pero se pueden simular con
#                   el uso de listas.
# {************************************}

if __name__ == '__main__':
    # Pilas
    pila = [3,4,5]
    pila.append(6)
    pila.append(7)
    #print(pila)
    pop = pila.pop()
    #print(pop)
    #print(pila)

    # Colas
    cola = deque([1,2,3,4])
    print(cola)
    cola.append(5)
    cola.append(6)
    print(cola)
    cola.popleft()
    print(cola)
