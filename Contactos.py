import os


class Nodo():
    def __init__(self, nombre, numero, apellido):
        self.item1 = nombre
        self.item2 = numero
        self.item3 = apellido
        self.siguiente = None
        self.anterior = None

class Contactos():
    def __init__(self):
        self.cabeza = None
    def insertar(self, nombre, numero,apellido):
        if self.cabeza is None:
            nuevo_nodo = Nodo(nombre,numero,apellido)
            self.cabeza = nuevo_nodo
            print("contacto agregado")
            return
        node = self.cabeza
        aux = False
        #recorrer lista para ver si exite numero
        while node is not None:
            if node.item3 == numero:
                aux =True
                node = node.siguiente
            else:
                node = node.siguiente
        if aux == True:
            print('El contacto ya existe')
        else:
            self.ordenar(nombre,numero,apellido)
            #node = node.siguiente
        #while node.siguiente is not None:
        #    node = node.siguiente
        #nuevo_nodo = Nodo(nombre,numero,apellido)
        #node.siguiente = nuevo_nodo
        #nuevo_nodo.anterior = node
        #print("el contacto se agrego")
    def recorre_lista(self):
        if self.cabeza is None:
            print('La lista no tiene elementos')
            return
        else:
            node = self.cabeza
            while node is not None:
                print("Apellido: ",node.item3,"Nombre:",node.item1,"Numero: ",node.item2)
                node = node.siguiente
    def insertar_antes(self,x,nombre,numero,apellido):
        if self.cabeza is None:
            print('Lista Vacia')
        else:
            node = self.cabeza
            while node is not None:
                if node.item3 == x:
                    break
                node = node.siguiente
            nuevo_nodo = Nodo(nombre,numero,apellido)
            nuevo_nodo.siguiente = node
            nuevo_nodo.anterior = node.anterior
            if node.anterior is not None:
                node.anterior.siguiente = nuevo_nodo
            node.anterior = nuevo_nodo
            print('contacto agregado')
    def insertar_despues(self,x,nombre,numero,apellido):
        if self.cabeza is None:
            print('Lista Vacia')
        else:
            node = self.cabeza
            while node is not None:
                if node.item3 == x:
                    break
                node = node.siguiente
            nuevo_nodo = Nodo(nombre,numero,apellido)
            nuevo_nodo.anterior = node
            nuevo_nodo.siguiente = node.siguiente
            if node.siguiente is not None:
                node.siguiente.anterior = nuevo_nodo
            node.siguiente = nuevo_nodo
            print('contacto agregado')
    def insertar_final(self,nombre,numero,apellido):
        if self.cabeza is None:
            nuevo_nodo = Nodo(nombre, numero, apellido)
            self.cabeza = nuevo_nodo
            return
        node = self.cabeza
        while node.siguiente is not None:
            node = node.siguiente
        nuevo_nodo = Nodo(nombre, numero, apellido)
        node.siguiente = nuevo_nodo
        nuevo_nodo.anterior = node
        print('contacto agregado')
    def insertar_principio(self,nombre,numero,apellido):
        if self.cabeza is None:
            nuevo_nodo = Nodo(nombre,numero,apellido)
            self.cabeza = nuevo_nodo
            return
        nuevo_nodo = Nodo(nombre,numero,apellido)
        nuevo_nodo.siguiente =self.cabeza
        self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
        print('contacto agregado')

    def ordenar(self,nombre,numero,apellido):
        node = self.cabeza
        while node is not None:
            aux = node.siguiente
            aux1 = node.anterior

            #print("Nodo Actual: ", node.item3,node.item1,node.item2)

            if aux is None:
                if aux1 is None:
                    aux2 = min(node.item3,apellido)

                    #print("Entrar si solo es uno")
                    if aux2 == apellido:
                        self.insertar_principio(nombre, numero, apellido)
                        #print('marca1')
                        break
                    else:
                        self.insertar_final(nombre, numero, apellido)
                        #print('marca2')
                        break
            if aux1 is None:
                if aux is not None:
                   #print('Entrando al principio de la lista')
                   #print(node.item3, aux.item3,apellido)
                   aux2 = min(node.item3,apellido,aux.item3)
                   aux3 = max(node.item3,apellido,aux.item3)
                   if node.item3 == apellido:
                       self.insertar_principio(nombre,numero,apellido)
                       break
                   elif aux2 == apellido:
                       self.insertar_principio(nombre, numero, apellido)
                       #print('marca5')
                       break

                   elif aux2 == node.item3:
                       if aux3 == aux.item3:
                            self.insertar_despues(node.item3,nombre, numero, apellido)
                            #print('marca6')
                            break
            #            break
            if aux is None:
                if aux1 is not None:
                    #print('Entrar a final de la lista')
                    #print(node.item3,apellido,aux1.item3)
                    aux2 = min(apellido,node.item3,aux1.item3)
                    aux3 = max(apellido,node.item3,aux1.item3)
                    if node.item3 ==apellido:
                        self.insertar_final(nombre, numero, apellido)
                        break
                    if apellido == aux3:
                        #print('marca10')
                        if aux1.item3 == aux2:
                            self.insertar_final(nombre,numero,apellido)
                            break

                    if aux2 == aux1.item3:
                        if aux3 == node.item3:
                            self.insertar_despues(node.item3,nombre, numero, apellido)
                            break

            if aux is not None:
                if aux1 is not None:
                    #print('Entra en el medio')
                    #print(node.item3,apellido,aux.item3)
                    aux2 = min(node.item3,apellido,aux.item3)
                    aux3 = max(node.item3,apellido,aux.item3)
                    if apellido == node.item3:
                        self.insertar_antes(node.item3,nombre, numero, apellido)
                        #print('marca8')
                        break
                    if aux2 == node.item3:
                        if aux3 == aux.item3:
                            self.insertar_antes(aux.item3,nombre, numero, apellido)
                            #print('marca9')
                            break
            node = node.siguiente
    def reporte(self):
        node = self.cabeza
        Graph = "digraph L {" + "\n"
        Graph = Graph + "node [shape = record, color = cornflowerblue];"+"\n"
        aux = self.cabeza
        auxCont = 0


        if node is None:
            return
        else:
            while node is not None:
                auxCont = auxCont + 1
                Graph = Graph + "nd_"+str(auxCont)+" "+"[label=\""+node.item3+"\\l"+node.item1+"\\l"+node.item2+"\" ]"+"\n"
                node = node.siguiente
        Graph = Graph + "\n"
        for num in range(auxCont +1):
            if num !=0 and num != auxCont:
                Graph = Graph +"nd_"+str(num)+"->"
            if num == auxCont:
                Graph = Graph+"nd_"+str(num)+"\n"
        Graph = Graph+"\n"+"}"
        print(Graph)
        nuevo_arch = open('cola.dot','w')
        nuevo_arch.write(Graph)
        nuevo_arch.seek(0)
        comando = "dot -Tpng lista.dot -o lista.png"
        os.system(comando)
        os.system('lista.png')




