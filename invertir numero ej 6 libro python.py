aux= int(0)
aux2=int(0)

n=int(input("ingrese numero entero: "))
for i in range (10,n):
    aux=(i % 10)
    i=i//10
    aux2= aux2*10+aux
aux2=aux2*10+i
print ("el numero invertido es: ", aux2)

