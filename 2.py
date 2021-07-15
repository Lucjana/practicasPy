#Escribir una función que reciba como parámetro una tupla conteniendo una fecha
#(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
#en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de
#2017". Escribir también un programa para verificar su comportamiento

def devolvercadena(fecha):
    cadena="Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    dia,mes,año=fecha
    mesecillo=""
    for i in range (len(cadena)):
        if i+1==mes:
            mesecillo=cadena[i]
    año=año+2000
    cadenanew= dia, mesecillo, año
    
    return cadenanew

fec=(12,10,17)
q=devolvercadena(fec)
dia,mes,año=q
print(dia, "de", mes, "de", año)
    
    
            