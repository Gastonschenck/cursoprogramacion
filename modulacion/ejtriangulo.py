def calculandotriangulos():
    area=float
    for i in range(1,100):
        area=calcularareadetriangulo(i,i*2)
        print (area)
def calcularareadetriangulo(base,altura):
    return ((base*altura)/2)
calculandotriangulos()