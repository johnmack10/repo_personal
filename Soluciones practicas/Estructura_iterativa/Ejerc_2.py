"""Mostrar sólo los números pares desde 0 hasta el número ingresado (input).
   Nota: para saber si un número es par hacer i % 2 == 0)"""
   
numeros = int(input("Ingrese la cantidad de numeros que quieres ver: "))   
for i in range(numeros + 1):
    if i % 2 == 0:
        print(i) 