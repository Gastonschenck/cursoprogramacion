import random
arreglo=[]
def cargar():
    tamanox=int(input("ingrese columnas: "))
    tamanoy=int(input("ingrese filas: "))
    for i in range (tamanox):
        fila=[]
        for j in range(tamanoy):
            fila=[random.randint(1,9) for _ in range(tamanoy) ]
        arreglo.append (fila)

def mostrar ():
    for fila in arreglo:
        for elemento in fila:
            print (elemento, end=" ")
        print () 

cargar ()
mostrar()