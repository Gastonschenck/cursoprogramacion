sueldo=float(input("ingrese el sueldo: "))
if sueldo>0 and sueldo<=15000:
    print ("sueldo + 20%: ", sueldo*1.2)
elif sueldo<20000:
    print ("sueldo + 10%: ", sueldo*1.1)
elif sueldo<25000:
    print ("sueldo + 5%: ", sueldo*1.05)
else:
    print ("sin aumento")

