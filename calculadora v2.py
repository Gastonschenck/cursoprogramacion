from pynput import keyboard as kb
import keyboard
import time
#def dibujar_calcularora():

def leerDatos ():
    valor=""
    aux=str
    num=0.0
    while True:
        valortecla=keyboard.read_key()
        time.sleep(0.5)
        if valortecla=="0":
            valor += "0"   
            #keyboard.press("backspace")
            print (valor)
        elif valortecla=="1":
            valor += '1'
            valortecla=""    
            #keyboard.press("backspace")
            num=float(valor)
            print(num)
            
        
        
        elif valortecla=="+" or valortecla=="-" or valortecla=="*" or valortecla=="/":
            operacion=valortecla
            print (operacion)
            #keyboard.press("backspace")
            return (num, operacion)
            break
        elif valortecla=="q":
            return ("q","q")
        
            #keyboard.press("backspace")


def hacerCuenta(num1,num2,operacion):
    if operacion =="+":
        return num1+ num2
    elif operacion=="-":
        return num1-num2
    elif operacion=="*":
        return num1*num2
    elif operacion=="/":
        return num1/num2

def calculadora ():
    resultado=0.0
    numero=0.0
    seguir=True
    while seguir==True:
        numero,op=leerDatos ()
        if op=="q":
            seguir=False
            break
        resultado=hacerCuenta(resultado,numero,op)
        #print (op, numero)
        print (resultado)

calculadora()

