import random
arreglo=[]
arreglouni=[]
fila=[]
def cargar():
    tamanox=int(input("ingrese columnas: "))
    tamanoy=int(input("ingrese filas: "))
    for i in range (tamanox):
        fila=[]
        for j in range(tamanoy):
            fila=[random.randint(1,9) for _ in range(tamanoy) ]
        arreglo.append (fila)

def pasar(matriz):
    return [numero for fila in matriz for numero in fila]
    
def mostrar():
    print (arreglouni)
cargar()
arreglouni=pasar(arreglo)
print(arreglouni)
mostrar()
