"""En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. 
    Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8)
    o bajo (promedio es inferior a 6). Desarrollar un algoritmo que resuelva este problema. 
    Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen."""
    
contador = 1
alumno =  0
suma_notas = 0
while alumno != 1:
    nota = float(input(f"Ingrese la nota de alumno {contador}: "))
    contador += 1
    suma_notas += nota 
    alumno = int(input("Para agregar otro alumno ingrese (0)\nPara salir ingrese(1) "))

resultado = suma_notas / (contador - 1)
if resultado > 8:
    print(f"El promedio del curso es elevado {resultado}")
elif resultado >=6 and resultado <=8:
    print(f"El promedio del curso es aceptable {resultado}")
else:
    print(f"El promedio es bajo {resultado}")




#Otra forma con el for
notas = [9, 8, 7, 6, 10, 8, 7, 6] 
suma_notas = 0
for nota in notas:
    suma_notas += nota

cantidad_estudiantes = len(notas)
resultado = suma_notas / cantidad_estudiantes

if resultado > 8:
    print(f"El promedio del curso es elevado {resultado}")
elif resultado >=6 and resultado <=8:
    print(f"El promedio del curso es aceptable {resultado}")
else:
    print(f"El promedio es bajo {resultado}")


