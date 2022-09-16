print("Ejercicio 15: Par o Impar")

NUM = int(input("Ingrese número del 1 al 10:"))

par_Impar = {
    1: 'Impar',
    2: 'Par',
    3: 'Impar',
    4: 'Par',
    5: 'Impar',
    6: 'Par',
    7: 'Impar',
    8: 'Par',
    9: 'Impar',
    10: 'Par'
}

print(par_Impar.get(NUM, "Numero fuera de Rango"))
