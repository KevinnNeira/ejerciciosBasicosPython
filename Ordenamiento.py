n = int(input("Ingrese el numero: "))
n1 = int(input("Ingrese el numero: "))

if n < n1:
    print(n,"Es numero menor entre",n1)
else:
    print(n1,"Es numero menor entre",n)


n = int(input("Ingrese el numero: "))
n1 = int(input("Ingrese el numero: "))
n2 = int(input("Ingrese el numero: "))

if n < n1:
    print(n,"Es numero menor entre",n1)
elif n2 < n and n2 < n1:
    print(n1,"Es numero menor entre",n)
else:
    print(n2,"Es numero menor entre",n,",",n1)