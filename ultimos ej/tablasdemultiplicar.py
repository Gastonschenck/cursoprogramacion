def inicializararray(filas,columnas):
    array =[[0 for _ in range(filas)] for _ in range(columnas)]
    return (array)

def guardartabla (size):
    tabla=[]
    tabla=inicializararray(size,size)
    for i in range(size):
        for j in range(size):
            tabla[i][j]=(i+1)*(j+1)
    return (tabla)

def mostrartabla( tabla ):
    for i in tabla:
        print('')
        print('TABLA del', i[0], end=' ')
        
        for j in i:
            if j>99:
                print (j, end='')
            elif j>9:
                 print (j, end=' ')
            else:
                print (j, end='  ')

def main():
    size=int(input('ingrese tamaño deseado: '))
    tablamulti=guardartabla(size)
    mostrartabla(tablamulti)
    
main()