horaact = int(input("Ingrese la hora actual: "))
canth = int(input("Ingrese la cantidad de horas: "))
horafut = horaact + canth
if(horafut > 12):
    a = int(horafut/12)
    x = a * 12
    b = horafut - x
    print(b)
else:
    print(horafut)