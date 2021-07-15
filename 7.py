#7. Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al 
#usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación.
#Finalizar el proceso al ingresar -1.
#Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
#inexistentes.

def eliminarnumeros(numeros):
    try:
        n=int(input("Ingrese un número a eliminar: "))
        while n != -1:
            numeros.remove(n)
            print(numeros)
            n=int(input("Ingrese un número a eliminar: "))
            
    except KeyError or ValueError:
        print("El valor no se ha encontrado")
    
    
    
numbers={1,2,3,4,5,6,7,8,10}
c=eliminarnumeros(numbers)
print(c)