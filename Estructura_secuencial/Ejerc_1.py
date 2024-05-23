"""Un estudiante está cursando 5 materias, tiene la nota de cada
   materia y quiere saber cuál es su promedio."""
   
"""EPS
Entrada:nota1 (float),nota2 (float), nota3 (float), nota4 (float), nota5 (float)
Salida: promedio = la suma de las 5 notas dividido 5
Proceso:Promedio (float)
"""
nota1 = float(input("Ingrese la nota de la primera materia: "))
nota2 = float(input("Ingrese la nota de la segunda materia: "))
nota3 = float(input("Ingrese la nota de la tercera materia: "))
nota4 = float(input("Ingrese la nota de la cuarta materia: "))
nota5 = float(input("Ingrese la nota de la quinta materia: "))

suma = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f"El promedio de nota de las materias es {suma}")


