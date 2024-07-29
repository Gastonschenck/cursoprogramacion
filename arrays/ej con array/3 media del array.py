media=[]
suma=0.0
for i in range (10):
    numero=input("ingrese un numero: ")
media.append(float(numero))
for i in range (10):
    suma=suma+media[i]
print ("el promedio es: ", suma/10)