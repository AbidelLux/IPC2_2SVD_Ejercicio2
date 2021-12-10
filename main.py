# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Contactos import Contactos
ListaContactos = Contactos()
def pedirNoMenu():
    print("Ingrese la opcion que desea")
    CorreccionOpc =True
    while(CorreccionOpc):
        try:
            num = int(input())
            CorreccionOpc = False
        except ValueError:
            print("Ingrese un numero entero")
    return num

def menu():
    while True:
        print("1. Ingresar Contacto")
        print("2. Visualiza Lista")
        print("3. Salir")

        opcion = pedirNoMenu()

        if opcion == 1:
            print('Ingresar Nombre: ')
            nombre = input()
            print('Ingresar numero')
            numero = input()
            ListaContactos.insertar(nombre,numero)
        elif opcion == 2:
            print("Lista")
            ListaContactos.recorre_lista()
        elif opcion == 3:
            break
        else:
            print('La opcion no existe')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
