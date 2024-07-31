#def dibujar_calcularora():

def leerDatos ():
    dato1=float(input("Numero: "))
    cuenta=(input("Operacion: "))
    dato2=float(input("Numero: "))
    
    return 5(dato1,dato2,cuenta)



def hacerCuenta(num1,num2,operacion):
    if operacion =="+":
        return num1+num2
    elif operacion=="-":
        return num1+num2
    elif operacion=="*":
        return num1*num2
    elif operacion=="/":
        return num1/num2

def calculadora ():
    seguir=True
    while seguir==True:
        numero1,numero2,op=leerDatos ()
        
        resultado=hacerCuenta(numero1,numero2,op)
        print (resultado)
        pregunta=input("desea seguir?  s/n")
        if pregunta=="n":
            seguir=False
        
calculadora()

