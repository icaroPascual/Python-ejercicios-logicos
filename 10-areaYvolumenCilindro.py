print("Ejercicio 10: CALCULAR ÁREA Y VOLUMEN DEL CILINDRO ")

PI = 3.1416

print("Ingrese Radio y Alto: ")
radio = float(input("radio: "))
alto = float(input("alto: "))


vol = PI * radio**2 * alto
area = 2*PI*radio*(radio + alto)


print("Volumen:", vol)
print("Area:", area)
