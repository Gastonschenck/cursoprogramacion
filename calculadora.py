from pynput import keyboard as kb
import keyboard
#def dibujar_calcularora():

def leerDatos ():
    
    def leerOp():
        while True:
            valor=keyboard.read_key()
            if valor=="+":
                signo="+"
                
                return signo
            elif valor=="-":
                signo="-"
                #keyboard.write(backspace)
                return signo
            elif valor =="*":
                signo="*"
                return signo
            elif valor =="/":
                signo="/"
                return signo    
    dato1=float(input("Numero: "))
    #lee teclas de operacion
    cuenta= leerOp ()
    #borra tecla presionada
    keyboard.press("backspace")
    #limpiar=input()
    #cuenta=(input("Operacion: "))
    dato2=float(input("Numero: "))
    return (dato1,dato2,cuenta)



def hacerCuenta(num1,num2,operacion):
    if operacion =="+":
        return num1+num2
    elif operacion=="-":
        return num1-num2
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

