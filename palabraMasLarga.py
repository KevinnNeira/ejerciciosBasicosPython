pal1 = str(input("Ingrese la palabra 1: "))
pal2 = str(input("Ingrese la palabra 2: "))
x = len(pal1)
x1 = len(pal2)
if x > x1:
    print("El orden segun la cantidad de letras en orden ascendente es: ",pal2,"(",x1,")",pal1,"(",x,")")
else:
    print("El orden segun la cantidad de letras en orden ascendente es: ",pal2,"(",x1,")"",",pal1,"(",x,")")