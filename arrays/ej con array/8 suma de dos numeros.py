arreglo=[]
cfilas=int(input ("ingrese la cantidad de sumas: "))
for i in range (cfilas):
    fila=[]
    numeroa=(int(input("ingrese primer numero: ")))
    numerob=(int(input("ingrese segundo numero: ")))
    fila=[numeroa, numerob, numeroa+numerob]
    arreglo.append (fila)

def mostrar ():
    for fila in arreglo:
        print (fila[0],"+",fila[1],"=",fila[2])

mostrar()
