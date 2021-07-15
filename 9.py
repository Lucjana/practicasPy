#Escribir una función que reciba un número entero N y devuelva un diccionario con
#la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar
#la función.

def tabladel12 (n):
    dic={}
    clave=0
    for i in range(13):
        if i != 0:
            clave=n*i
            dic[i]=str(clave)
    return dic


q=tabladel12(n=4)
print(f"\nLa tabla de {q} es: ", q)