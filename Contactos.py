class Nodo():
    def __init__(self, nombre, numero):
        self.item1 = nombre
        self.item2 = numero
        self.siguiente = None

class Contactos():
    def __init__(self):
        self.cabeza = None
    def insertar(self, nombre, numero):
        if self.cabeza is None:
            nuevo_nodo = Nodo(nombre,numero)
            self.cabeza = nuevo_nodo
            return
        node = self.cabeza
        while node.siguiente is not None:
            node = node.siguiente
        nuevo_nodo = Nodo(nombre,numero)
        node.siguiente = nuevo_nodo
        print("el contacto se agrego")
    def recorre_lista(self):
        if self.cabeza is None:
            print('La lista no tiene elementos')
            return
        else:
            node = self.cabeza
            while node is not None:
                print(node.item1," ",node.item2)
                node = node.siguiente
