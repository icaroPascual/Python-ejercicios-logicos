print("Ejercicio 13: Verificar si el año es bisiesto")


Year = int(input("Ingrese año: "))

if (Year % 400 == 0) or (Year % 4 == 0) and (Year % 100 != 0):
    print("El año es Bisiesto")
else:
    print("El año no es Bisiesto")
