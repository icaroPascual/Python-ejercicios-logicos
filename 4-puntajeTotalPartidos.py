print("Puntaje total de partidos")

print("ingrese el total de partidos ganados")
pg=int(input())
print("ingrese el total de partidos perdidos")
pp=int(input())
print("ingrese el total de partidos empatados")
pe=int(input())

ppg=pg*1
ppp=pp*-1
ppe=pe*0

pf=ppg+ppp+ppe

print("El puntaje total obtenido es: ",pf)