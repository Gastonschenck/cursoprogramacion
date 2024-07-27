
arreglo=[]
tamano=int(input("ingrese cantidad de nombres: "))
for i in range (tamano):
    fila=[]
    nombre=str(input("ingrese un nombre: "))
    contar=str( len(nombre))
    fila.append(nombre)
    fila.append(contar)
    arreglo.append(fila)
for fila in arreglo:
    print ("el nombre", fila[0], ", tiene:", fila[1], "letras")