from pynput import keyboard as kb
import keyboard

valor1=0
valor2=0
while True:
    valortecla=keyboard.read_key()
    if valortecla=="+" or valortecla=="-" or valortecla=="*" or valortecla=="/":
        operacion=valortecla
        keyboard.press("backspace")
        valor1=float(input())
        keyboard.press ("enter")
        print (valor1)
        break
        #hacerCuenta (valor1,valor2,valortecla)