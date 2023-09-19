##############################################################################
#Elaborado por: Alejandro Madrigal y Daniel Campos
#Fecha de creación: 18-9-2023 Hora: 8:08 am
#Última edición:
#Versión: 3.11.4 64bits
##############################################################################
import random
#Listas
numero=list(range(1,100))
#Reto 3
def sacarPares(a):
    """
    """
    lista=crearLista(cant)
    for a in lista:
        if a%2 == 0:
            return True
        return False
def crearLista(cant):
    """
    """
    lista=[]
    if cant>0:
        lista = [random.randint(1, 99) for a in range(cant)]
    return lista
def  modificarLista(lista):
    """
    """
    lista=crearLista(cant)
    listaNueva=[]
    for a in lista:
        if sacarPares(a)==True:
            listaNueva.append(0)
        else:
            listaNueva.append(1)
    return listaNueva

cant=int(input("Ingrese la cantidad de elementos que desea en su lista: "))
print(crearLista(cant), modificarLista(lista=crearLista(cant)))
