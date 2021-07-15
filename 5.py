#En geometría un vector es un segmento de recta orientado que va desde un punto
#A hasta un punto B. Los vectores en el plano se representan mediante un par ordenado de números reales (x, y) llamados componentes.
#Para representarlos basta con unir el origen de coordenadas con el punto indicado en sus componentes:
#Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo basta calcular su producto escalar y verificar si es igual
#a 0. Ejemplo:
#A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
#Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales o no.

def vectores (a,b):
    x,y=a
    q,w=b
    multiplicacion=((x)*(q))+((y)*(w))
    if multiplicacion == 0:
        return True
    else:
        return False
    
    

q=vectores((2,3),(3,2))
if q:
    print("Son ortogonales")
else:
    print("No son ortogonales")
    