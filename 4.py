#4. Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
#son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
#o False. Escribir también un programa para verificar su comportamiento.

def domino(tup1, tup2):
    q=0
    bandera=False
    for i in range (len(tup2)):
        for q in range (len(tup1)):
            if tup2[i]==tup1[q]:
                   bandera=True
    return bandera

tup1= (3,6)
tup2=(5,4)
print(domino(tup1,tup2))