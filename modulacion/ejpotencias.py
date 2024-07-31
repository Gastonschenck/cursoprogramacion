def potencia(b,e):
    if e==0:
        return (1)
    else:    
        for i in range (1,e):
            pot=b*b
        return (pot)


def leerdatos():
    base=int(input("ingrese base: "))
    exponente=int (input("ingrese exponente: "))
    while exponente<0:
        exponente=int(input("ingrese exponente mayor que 0"))
    print(potencia(base,exponente))

leerdatos()