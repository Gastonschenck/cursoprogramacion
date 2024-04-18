#leer numero por teclado si <= 0 salir, sino mostrar raiz  y cuadrado
Num=float(input("ingrese un numero"))
if Num>0:
    print("Numero: ", Num, "\nCuadrado: ",Num**2, "\nRaiz: ",Num**0.5)
else:
    print ("-----ERROR-----")
