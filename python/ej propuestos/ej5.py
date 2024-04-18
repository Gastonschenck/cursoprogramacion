#tres numeros si el primero es negativo: producto, sino suma
print("Ingrese tres numeros: ")
N1=float(input ("Num1: "))
N2=float(input ("Num2: "))
N3=float(input ("Num3: "))
if N1<0:
    print("producto de los tres numeros: ", N1*N2*N3)
else:
    print ("suma de los tres numeros: ", N1+N2+N3)
    