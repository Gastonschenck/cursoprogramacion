tablero=["-","-","-","-","-","-","-","-","-"]
#def inicializar():

#raiz
def empezar():
    ganador=False
    empate=False
    jugador="X"
    cant_jugadas=0
    while ganador==False and cant_jugadas<9:
        
        if jugador=="O":
            jugador="X"
        else:
            jugador="O"
        dibujar_tablero(jugador)
        jugada(jugador)
        ganador=hay_ganador()
        cant_jugadas+=1
        if cant_jugadas==9 and ganador==False:
            jugador="EMPATE"
    dibujar_tablero("termino")
    dibujar_gano(jugador)

    
def hay_ganador():
    ganador=False
    if tablero[0] == tablero[1] == tablero [2] != "-":
        ganador=True
    elif tablero[3] == tablero[4] == tablero [5]!= "-":
        ganador=True
    elif tablero[6] == tablero[7] == tablero [8]!= "-":
        ganador=True
    elif tablero[0] == tablero[3] == tablero [6]!= "-":
        ganador=True
    elif tablero[1] == tablero[4] == tablero [7]!= "-":
        ganador=True
    elif tablero[2] == tablero[5] == tablero [8]!= "-":
        ganador=True
    elif tablero[0] == tablero[4] == tablero [8]!= "-":
        ganador=True
    elif tablero[2] == tablero[4] == tablero [6]!= "-":
        ganador=True
    return (ganador)

#el jugador elije el numero y se guarda en tablero
def jugada(valor):
    vacio=False
    posicion=1
    while vacio==False:
        posicion=int(input("ingrese un numero: "))
        posicion-=1
        if posicion > -1 and posicion < 9:
            if tablero[posicion]=="-" :
                vacio=True
    tablero[posicion]=valor
    

#dibuja el tablero
def dibujar_tablero(valor):
    print()
    print("jugador: ", valor)
    print()
    print (tablero[0],"|", tablero[1],"|", tablero [2],"  1|2|3")
    print (tablero[3],"|", tablero[4],"|", tablero [5], "  4|5|6")
    print (tablero[6],"|", tablero[7],"|", tablero [8], "  7|8|9")

#dibuja el ganador

def dibujar_gano(valor):
    print (valor)

empezar()