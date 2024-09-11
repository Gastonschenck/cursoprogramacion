coloraula=['azul','verde','amarilla']
capaula=[40,35,30]
capaulaaux=50
cantalumnos=int(input('ingrese cantidad de alumnos: '))
for i in range (0,len(capaula)):
    if capaula[i] >=cantalumnos and capaula[i]<capaulaaux:
        aula=i
        capaulaaux=capaula[i]
print (f'el aula adecuada es la: {coloraula[aula]}')

        