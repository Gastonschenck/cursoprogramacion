import random
def main():
    edificio=[[random.randint(1,8) for _ in range(2)] for _ in range (10)]
    totalpisos=[]
    totaledificio=0
    for i in edificio:
        acumpiso=0    
        for j in i:
            acumpiso += j
        print(i,' Total x piso: ',acumpiso)
        totalpisos.append(acumpiso)
        totaledificio+=acumpiso
    print('Total de habitantes edificio: ',totaledificio)
main()