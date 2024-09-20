def cargar (): #cargar nombre paciente diagnostico y tratamieneto
    datos=["","",0]
    datos[0]=str(input("Ingrese Nombre: "))
    datos[1]=str(input("Ingrese Diagnostico: "))
    datos[2]=float(input("Ingrese precio tratamiento"))
    return (datos)
def buscarPaciente(matriz):#Liste los pacientes que tienen un costo de tratamiento mayor a un valor dado
    monto=float(input("Ingrese el monto: "))
    pacientesCaros=[i for i in matriz if i[2]>=monto]#guarda todos los datos de pacientes con tratamientos caros
    nombresPacientesCaros=[i[0] for i in pacientesCaros]#guarda solo los nombres...
    print (nombresPacientesCaros)
    

def main():
    opcion=0
    matrizPaciente=[]
    costoTotal=0.0
    matrizPaciente=[["gas","l",50],["juan","l",100],["jav","lasas",300]]
            
    while opcion!=4: 
        print ("Opciones:")
        print("1- Cargar nuevo paciente")
        print("2- Costo total tratamientos")
        print("3- seleccionar pacientes por costo tratamiento")
        print("4-Salir")
        print("")
        opcion=int(input())
        if opcion==1:
            matrizPaciente.append(cargar())
        elif opcion==2:
            costo=[i[2] for i in matrizPaciente]#hace lista con los precios de tratamiento
            costototal= sum (costo)
            print (costototal)
        elif opcion==3:
            buscarPaciente(matrizPaciente)
            
main()
