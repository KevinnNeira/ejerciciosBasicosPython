num1 = int(input("Ingrese la nota del ceratmen 1: "))
num2 = int(input("Ingrese la nota del certamen 2: "))
labo = int(input("Ingrese la nota del laboratorio: "))

nf = 0
num3 = 0 

while nf < 60:
    nc = (num1 + num2 + num3) /3
    nf = (nc * 0.7) + (labo * 0.3)
    num3 = num3 + 1
    if nf == 60:
        break
    
print(f"""Necesita una nota de {num3} en el certamen 3""")