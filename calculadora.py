from pynput import keyboard as kb
import keyboard
#def dibujar_calcularora():

def leerDatos ():
    cuenta=str
    def leerSigno(signo):
        global cuenta
        if signo==kb.KeyCode.from_char("+") or signo=="-" or signo=="*" or signo=="/" :
            cuenta=str(signo)
            #print (cuenta)
            return False
            
        keyboard.write (key.backspace)
    dato1=float(input("Numero: "))
    #with kb.Listener(leerSigno) as escuchador:
    #   escuchador.join()
    #lee y comprueba la operacion
    kb.Listener(leerSigno).run()
       #limpiar=input()
    #cuenta=(input("Operacion: "))
    dato2=float(input("Numero: "))
    return (dato1,dato2,cuenta)



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

