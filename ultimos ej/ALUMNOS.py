#cargar alumnos, notas y promedio.
def cargar ():
    i=1
    notas=[0]*4
    nombre= input ('Nombre Alumno: ')
    for i in range (1,4):
        
        nota=int(input(f'ingrese nota trimestre {i}:'))
        while nota<1 or nota>10:
            nota=int(input('ingrese numero entre 1 y 10'))
        notas[i]=nota
    return (nombre, notas)

def promedio(notas):
    acum=0
    for i in range (1,4):
        acum+=notas[i]
    return (acum/3)

def buscar(alumnos):
    buscado=input('Nombre a buscar: ')
    for i, alumno in enumerate (alumnos):
        if alumno==buscado:
            return (i)
    return (-1)

def main():
    opcion=''
    notas=[]
    nombres=[]
    cont=0
    indice=0
    while opcion!='3':
        print('‐---------------------------------')
        print ('Que desea hacer?')
        print('1: Cargar alumno')
        print ('2: Promedio alumno')
        print ('3: Salir')
        opcion=str(input())
        if opcion=='1':
            nombresaux, notasaux=cargar()
            nombres.append(nombresaux)
            notas.append(notasaux)
            cont+=1
        elif opcion=='2':
            indice=buscar (nombres)
            if indice==-1:
                print("Nombre no encontrado")
            else:              
                promedioalumno= promedio(notas[indice])
                print("El promedio de: ", nombres[indice], "es: ", promedioalumno)
        elif opcion=='3':
            print ('Chau!')
        else:
            print ("Opcion incorrecta")
main ()
            
            
            
            
    
    