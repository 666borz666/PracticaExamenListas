##############################################################################
#Elaborado por: Alejandro Madrigal y Daniel Campos
#Fecha de creación: 18-9-2023 Hora: 8:08 am
#Última edición:
#Versión: 3.11.4 64bits
##############################################################################
import random
#Reto 3
def crearLista(cant):
    lista = [random.randint(1, 99) for _ in range(cant)]
    return lista

def sacarPares(a):
    if a % 2 == 0:
        return True
    else:
        return False
    
def modificarLista(lista):
    listaNueva = []
    for a in lista:
        if sacarPares(a):
            listaNueva.append(0)
        else:
            listaNueva.append(1)
    return listaNueva

#Reto 9
def productoCartesiano(A, B):
    """
    """
    nuevaLista=[]
    for a in A:
        for b in B:
            nuevaLista.append([a]+[b]) 
    return nuevaLista

#Reto 10

#programa principal

"""
#Reto 3
cant = int(input("Ingrese la cantidad de elementos que desea en su lista: "))
lista = crearLista(cant)
print("Lista original:", lista)
print("Lista modificada:", modificarLista(lista))
"""

"""
#Reto 9
A=[1,2]
B=["x","y","z"]
print(productoCartesiano(A, B))
A=[1,2,3,4]
B=["a","b"]
print(productoCartesiano(A, B))
"""

#Reto 10