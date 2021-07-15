def leerentero(texto="Ingrese un número entero"):
    while True:
        try:
            n = int(input(texto+": "))
            break
        except ValueError:
            print("Sólo se permiten números. Intente nuevamente.\n")
    return n    

def esprimo(n, divisor=2):
    if abs(n)<=divisor:
        return True
    else:
        return False if n%divisor==0 else esprimo(n, divisor+1)

def imprimirprimos(a, b):
    if a<=b:
        if esprimo(a):
            print(a, end=" ")
        imprimirprimos(a+1, b)

# Programa principal
a = leerentero()
b = leerentero("Ingrese un número mayor o igual que "+str(a))
while a>b:
    print("El primer valor debe ser menor o igual que el segundo.\n")
    a = leerentero()
    b = leerentero("Ingrese un número mayor o igual que "+str(a))
print(f"\nNúmeros primos entre {a} y {b}:")
imprimirprimos(a,b)