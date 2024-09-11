def multiplicarArreglo (arreglo1,arreglo2):
    multiplicacion=[]
    i=0
    for i in range (len(arreglo1)):
        multiplicacion.append(arreglo1[i]*arreglo2[i])
    return (multiplicacion)
def main():
    resultadofinal=[]
    v1=[1,2,3]
    v2=[4,5,6]
    v3=[2,1,2]
    v4=[1,2,1]
    resultado1=multiplicarArreglo(v1,v2)
    resultado2=multiplicarArreglo(v3,v4)
    resultadofinal= multiplicarArreglo (resultado1,resultado2)
    print(resultadofinal)
main()
    