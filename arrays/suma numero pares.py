lista = []
n=int (input("cantidad de numeros: "))
i=1
while i <=n:
    num=int(input("ingrese un numero: "))
    lista.append(num)
    i+=1
suma=0
j=0
while j<len(lista):
    if lista[j]%2==0:
        suma+=lista[j]
    j+=1
print ("la suma de numeros pares ingresado es de: ", suma)
