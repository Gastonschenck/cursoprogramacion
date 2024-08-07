from pynput import keyboard
from os import system
import keyboard
import time
#def dibujar_calcularora():
valor=""
#def dibujar ():
    
def leerDatos ():
    
    aux=str
    num=0.0
    def cargarNumero (valortecla): 
        global valor
        if valortecla=="0":
            valor += '0'   
        elif valortecla=="1":
            valor += '1'
        elif valortecla=="2":
            valor += '2'
        elif valortecla=="3":
            valor += '3'
        elif valortecla=="4":
            valor += '4'
        elif valortecla=="5":
            valor += '5'
        elif valortecla=="6":
            valor += '6'
        elif valortecla=="7":
            valor += '7'
        elif valortecla=="8":
            valor += '8'
        elif valortecla=="9":
            valor += '9'
        
        valortecla=""    
        num=float(valor)
        print(valor,end='\r')
        return(num)
    while True:
        with keyboard.() as listener:
            listener.join()
        
        
        
        #espera un instante
        time.sleep(0.1)
        if valortecla=="0" or valortecla=="1" or valortecla=="2" or valortecla=="3" or valortecla=="4" or valortecla=="5" or valortecla=="6" or valortecla=="7" or valortecla=="8" or valortecla=="9":
         num=cargarNumero(valortecla)
        
            
        
        
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
    numero=1.0
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
