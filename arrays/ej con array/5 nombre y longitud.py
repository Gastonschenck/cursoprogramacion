from collections import Counter
nombres=[]
longitud=[]
tamano=int(input("ingrese cantidad de nombres: "))
for i in range (tamano):
    nombre=str(input("ingrese un nombre: "))
    nombres.append(nombre)
    contar= len(nombre)
    longitud.append(contar)
print (nombres)
print (longitud)
for i in range (tamano):
    print (nombres[i], " tiene ", longitud[i]," letras")