#Modificar el algoritmo anterior, de forma que, si se teclea un cero, se vuelva
#a pedir el número por teclado (así hasta que se teclee un número mayor que
#cero) (recuerda la estructura mientras).
num=0
while num<=0:
    num= int(input("Ingrese un numero entero: "))
    if num/2==0:
        print("el numero no es par ni impar")
    elif num%2==0:
        print("el numero es par")
    else:
        print("el numero es impar")