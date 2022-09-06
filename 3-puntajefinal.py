print("Calcular puntaje final")

print("ingrese el numero de respuestas correctas")
rc=int(input())
print("ingrese el numero de respuestas incorrectas")
ri=int(input())
print("ingrese el numero de respuestas en blanco")
rb=int(input())

prc=rc*3
pri=ri*-1
prb=rb*0

pf=prc+pri+prb

print("El puntaje final es: ",pf)