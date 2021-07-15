#Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
#20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.

def generardiccionario():
    diccionario={}
    for i in range(1,20):
        diccionario[i]=i**2
    for i in diccionario:
        print("Clave: ", i, "valor: ", diccionario[i])
    
    
generardiccionario()
        
        
    
    