print("Ejercicio 12: Sueldo a percibir")

Sue = float(input("ingrese sueldo: "))

if Sue < 1000:
    Aum=Sue*0.15
    Sue=Sue+Aum

print("Su nuevo sueldo es: ",Sue)