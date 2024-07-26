fila=[]
arreglo=[]
tamano=int(input("ingrese cantidad de nombres: "))
for i in range (tamano):
    nombre=str(input("ingrese un nombre: "))
    contar=str( len(nombre))
    fila.append(nombre)
    fila.append(contar)
    arreglo.append(fila)
for fila in arreglo:
    print (fila)
   