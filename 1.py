#Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa para verificar su comportamiento:
#a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
#válida.
#b. Sumar N días a una fecha.
#c. Ingresar un horario desde teclado, verificando que sea correcto.
#d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
#segundo se considerará que el primero corresponde al día anterior. En ningún
#caso la diferencia en horas puede superar las 24 horas.
def esbisiesto(año):
    bisiesto=False
    if año%4==0 and año%100!=0 or año%400==0:
        bisiesto=True
    return bisiesto

def fechavalida(fecha):
    dia,mes,año=fecha
    valida=False
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia>=1 and dia <=31:
            valida=True
    if mes==4 or mes ==6 or mes == 9 or mes == 11:
        if dia >=1 and dia <=30:
            valida=True
    if mes==2 and esbisiesto(año)==True:
        if dia >=1 and dia <=29:
            valida=True
    if mes ==2 and esbisiesto(año)==False:
        if dia >=1 and dia <=28:
            valida=True
    return valida

def sumarfecha(fecha):
    dia, mes, año=fecha
    s=int(input("Cuandos días le gustaria sumar? "))
    suma= dia + s
    if suma > 31:
        suma=suma-31
        if mes < 12:
            return suma, mes+1, año
        else:
            return suma, (mes+1)-12, año+1
    
            
def ingresarfecha():
    dia=int(input("Ingrese día: "))
    mes=int(input("Ingrese mes: "))
    año= int(input("Ingrese año: "))
    fecha=(dia, mes, año)
    if fechavalida(fecha)==True:
        return fecha
    else:
        print("Fecha no válida")
        
def calcularhorario():
    hora=int(input("Escribir un horario válido: "))
    minutos=int(input("Escribir minutos: "))
    hora2=int(input("Escribir un horario válido: "))
    minutos2=int(input("Escribir minutos: "))
    resta=()
    newhour=0
    newminute=0
    if hora >= 0 and hora <=23 and hora2>=0 and hora2 <=23:
        if minutos >=0 and minutos <=59 and minutos2>=0 and minutos2<=59:
            if hora > hora2:
                newhour= (hora-hora2)+24
                if minutos>minutos2:
                    newminute=minutos-minutos2
                else:
                    newminute=minutos2-minutos
            else:
                newhour=hora2-hora
                if minutos>minutos2:
                    newminute=minutos-minutos2
                else:
                    newminute=minutos2-minutos
    resta=(newhour,newminute)
    return resta
                
            
    
fec=ingresarfecha()
su=sumarfecha(fec)
if fec != None:
   print("El día es: ", su)
   hour=calcularhorario()
   print("La diferencia es: ", hour)
   
   