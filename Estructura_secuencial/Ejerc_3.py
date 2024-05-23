"""Un hincha de fútbol desea conocer la cantidad de puntos que su
equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que
el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
recibe un punto, por cada partido ganado tres puntos y por los perdidos cero
puntos."""

"""EPS
Entrada: ganados(int), empatados(int), perdidos(int)
Proceso: puntos_ganados = multiplicar los ganados por 3
         puntos_empatados = multiplicar los empatados por 1
         puntos_totales = sumar todos los puntos
Salida:total_puntos(int)"""


perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))
empatados = int(input("Ingrese la cantidad de partidos empatados: "))
ganados = int(input("Ingrese la cantidad de partidos ganados: "))

puntos_empatados = empatados * 1

puntos_empatados = ganados * 3

puntos_totales = puntos_empatados + puntos_empatados

print(f"La cantidad total de puntos acumulados es: {puntos_totales}")
