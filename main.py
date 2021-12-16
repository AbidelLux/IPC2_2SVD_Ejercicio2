# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import xml.etree.ElementTree as ET
from Contactos import Contactos
ListaContactos = Contactos()
import os

def pedirNoMenu():
    print("Ingrese la opcion que desea")
    CorreccionOpc =True
    num = 0
    while(CorreccionOpc):
        try:
            num = int(input())
            CorreccionOpc = False
        except ValueError:
            print("Ingrese un numero entero")
    return num
def cargar_xml(rt,lista):
    tree = ET.parse(rt)#crear arbol apartir de xml
    root = tree.getroot()#buscar por etiqueta
    global t,a,n
    print('-------------------------------------')
    for element in root:
        print('nombre: ',element.find('nombre').text)
        print('apellido: ',element.find('apellido').text)
        print('telefono: ',element.find('telefono').text)
        print("**********************************")
        lista.insertar(element.find('nombre').text,element.find('telefono').text,element.find('apellido').text)
        print("**********************************")
    print('---------archivo cargado------------')


def menu():

    while True:
        print("1. Ingresar Contacto")
        print("2. Visualiza Lista")
        print("3. graph")
        print("4. Salir")

        opcion = pedirNoMenu()

        if opcion == 1:
            rt = input('Ingresar la ruta del archivo')
            cargar_xml(rt,ListaContactos)
            #print('Ingresar Nombre: ')
            #nombre = input()
            #print('Ingresar apellido: ')
            #apellido = input()
            #print('Ingresar numero: ')
            #numero = input()
            #ListaContactos.insertar(nombre,numero,apellido)
        elif opcion == 2:
            print("Lista")
            ListaContactos.recorre_lista()
        elif opcion == 3:
            ListaContactos.reporte()
        elif opcion == 4:
            break
        else:
            print('La opcion no existe')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
