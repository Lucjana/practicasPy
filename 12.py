#Crear una función contarvocales(), que reciba una palabra y cuente cuántas letras
#"a" contiene, cuántas "e", cuántas "i", etc. Devolver un diccionario con los resultados. Desarrollar un programa para leer una frase e invocar a
#la función por cada
#palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales
#hallada

def contarvocales(palabra):
    dic={}
    for letra in palabra:
        if letra in ["a","e","i","o","u"]:
            if letra not in dic:
                dic[letra]=1
            else:
                dic[letra]=dic[letra]+1
    return dic

frase=input("Ingrese frase: ")
palabras= frase.split()
for palabra in palabras:
    dic=contarvocales(palabra)
    lista=list(dic)
    if lista:
        for i in lista:
            print(f"la cantidad de veces que se repita la letra:{i} en la palabra {palabra} es {dic[i]}")
    else:
        print("La palabra no tiene vocales")
        
            
        
    
    


                
                
            
        
    