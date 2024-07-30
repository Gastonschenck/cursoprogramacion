arreglo =[]
for i in range (11):
    fila=[i+1 *numero if i==0 or numero==0  else i*numero for numero in range(11)]
    arreglo.append(fila)
print (arreglo)
for fila in arreglo:
    for numero in fila:
        if numero<10:
            print(numero, end="   ")
        else:
            print(numero, end="  ")
        
    print ()