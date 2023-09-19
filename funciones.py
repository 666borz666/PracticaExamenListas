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

#Reto 12

#Reto 13
def encontrarCiudadanos(n,cedulas):
    """
    """
    provincia=""
    ced=[]
    if n>=1 or n<=7:
        for a in cedulas:
            cedula=str(a)
            provincia=int(cedula[0])
            if provincia==n:
                ced.append(a)
        return ced
    else:
        return print("La provincia debe ser un valor entre 1 y 7.")
        
        
#Reto 14
def extraerNumeros(txt):
    """
    """
    num=[]
    numero = ""
    for a in txt:
        if a.isdigit() or a == ".":
            numero += a 
        elif numero:
            num.append(float(numero))
            numero = ""
    if numero:
        num.append(float(numero))
    return num

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

#Reto 13
print(encontrarCiudadanos(2,[123456789, 201340789, 222222222 ,433333333, 511111111, 207890456]))
print(encontrarCiudadanos (1,[123456789,213456789,222222222,233333333,511111111,207890456]))
print(encontrarCiudadanos (3,[123456789,213456789,222222222,423333333,511111111,207890456]))
print((9,[123456789,213456789,222222222,233333333,511111111,207890456]))

"""
#Reto 14
print(extraerNumeros("xy225p30ab0g8.9iou1000"))
print(extraerNumeros("ab95.8124c76n"))
print(extraerNumeros("x0.25za10.5"))
print(extraerNumeros("xyz"))
"""