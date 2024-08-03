from pynput import keyboard as kb
import keyboard

while True:
    if keyboard.read_key () == "+":
        print ("presiono mas")
        break
    print (keyboard.read_key())