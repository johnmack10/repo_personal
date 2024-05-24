"""Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin"""
"""EPS
Entrada: Nombre (Str)
Proceso: Ingresa cualquier nombre y junto a un while cuando ingresa fin se finaliza.
Salida: Salida del programa¿? """
nombre = " "
while nombre != "fin":
    nombre = input("Ingresa el nombre de la persona: (fin para salir) ").lower()
    
    