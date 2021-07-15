#Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
#repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
#ordenadas según su longitud.

def conjuntos(lis):
    q=lis.split()
    for i in range(len(q)):
        if "," in q:
            q.remove(q[i])
        else:
            c=set(q)
    return c

q="Hola como estas estas bien?"
p=conjuntos(q)
print(p)