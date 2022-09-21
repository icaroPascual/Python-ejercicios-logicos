print("Vector 1: Lectura de elementos enteros")

i = 1
F = []

print("Ingrese numero de elementos a Ingresar")
numElements = int(input())

while i <= numElements:
    element = int(input("Ingrese elemento: "))
    F.append(element)

    i = i+1

print(F)
