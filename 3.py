#Desarrollar un programa que utilice una función que reciba como parámetro una
#cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
#una tupla con las distintas partes que componen dicha dirección. Ejemplo:
#alguien@uade.edu.ar -> (alguien, uade, edu, ar).


def recibirmail(correo):
    resul=()
    lista=correo.split("@")
    lista=[lista[0]]+lista[1].split(".")
    for i in range(len(lista)):
        resul=resul+(lista[i],)
    return resul
        
    
    

t="alguien@uade.edu.ar"
print(recibirmail(t))