#. Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario y una lista de claves.
#La función debe eliminar del diccionario todas las claves
#contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad
#que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.

def eliminarclaves(dic):
    lista=[1,2,4]
    for i in lista:
        if i in dic:
            del dic[i]
        else:
            print(f"El valor {i} no existe")
    print (dic)

dic = {1:'Javier', 2:'Lucas',3:'Pedro'}
q=eliminarclaves(dic)
print(q)