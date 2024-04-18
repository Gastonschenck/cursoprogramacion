#distancia entre dos puntos
print ("ingrese coordenadas para el primer punto")
X1=int (input ("ingrese X del punto 1: "))
Y1=int (input ("ingrese Y del punto 1: "))
print ("ingrese coordenadas para el segundo punto")
X2=int ( input ("ingrese X del punto 2: "))
Y2=int (input ("ingrese Y del punto 2: "))
print ("la distancia es: ", (abs(X2-X1)**2+abs(Y2-Y1)**2)**0.5)