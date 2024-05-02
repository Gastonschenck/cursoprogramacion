#Realizar un algoritmo que, dado un número entero, visualice en pantalla si
#es par o impar. En el caso de ser 0, debe visualizar “el número no es par ni
#impar” (para que un número sea par, se debe dividir entre dos y que su resto
#sea 0)
num= int(input("Ingrese un numero entero: "))
if num/2==0:
    print("el numero es 0")
elif num%2==0:
    print("el numero es par")
else:
    print("el numero es impar")
    

