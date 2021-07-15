#12. Una librería almacena su lista de precios en un diccionario. Diseñar un programa
#para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
#listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
#costoso que venden en el comercio.
import random
listadeprecio={}
for i in range (3):
    clave=input("Nombre del libro? ")
    n=float(input("Precio: "))
    listadeprecio[clave]= n
for i in listadeprecio:
    listadeprecio[i]=((listadeprecio[i]*15)/100) + listadeprecio[i]
for i in listadeprecio:
    print("El valor de: ", i, "es: ", listadeprecio[i])
print(max(listadeprecio.values()))
    

