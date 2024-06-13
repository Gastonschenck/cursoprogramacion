resultado=float (0.0)
num=int (input("ingrese un numero: "))
for i in range (1,num+1):
    if i % 2==0:
        print (resultado, "-(1/",i, ") " )
        resultado=resultado-(1/i)
        
    else:
        
        print (resultado,"+(1/",i, ") ",  )
        resultado=resultado+(1/i)
        
print ("el total es: ", resultado)
