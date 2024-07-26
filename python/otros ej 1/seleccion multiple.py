expresion=int(input("ingrese la posicion "))
match expresion:
    case 1:
        print ("medalla de oro")
    case 2:
        print ("medalla de plata")
    case 3:
        print ("medalla de bronce")
    case _:
        print ("mencion de participacion")
        