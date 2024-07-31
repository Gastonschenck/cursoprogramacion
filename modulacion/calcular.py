def suma(numero1,numero2):
    return numero1+ numero2

def resta(numero1,numero2):
    return numero1- numero2
def division(numero1,numero2):
    return numero1/ numero2
def multiplicacion(numero1,numero2):
    return numero1* numero2


def calcularresultado():
    num1=input("ingrese primer numero" )
    operacion=input("ingrese operacion")
    num2=input("ingrese segundo numero")
    if operacion=="+":
        resultado=suma(num1,num2)
    if operacion=="-":
        resultado=resta(num1,num2)
    if operacion=="/":
        resultado=multiplicacion(num1,num2)
    if operacion=="*":
        resultado=division(num1,num2)
def mostrarresultado():
    print()
        