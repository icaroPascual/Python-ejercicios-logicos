import math

print("Numero de micro discos de 3.5 necesarios")

print("Ingrese Gb")
gb = float(input())

mg = gb*1024
md = mg/1.44

print("El numero de micro discos necesarios es: ",math.ceil(md))
