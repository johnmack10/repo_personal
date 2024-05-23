"""Un pintor de casas debe hacer un presupuesto para un cliente. Lo
que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
cliente le indica que necesita conocer el costo de mano de obra para pintar una
pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
pintar la pared."""

"""EPS
Entrada: altura(float), ancho(float), monto_fijo(float)
Proceso: area = altura * ancho (para saber la cantidad de metros cuadrados)
         costo = cant_m2 * monto_fijo (costo final de la mano de obra por todos los metros cuadrados)
Salida: costo (float)"""


altura = float(input("Ingrese la altura de la pared en metros: "))
ancho = float(input("Ingrese el ancho de la pared en metros: "))
monto_fijo = float(input("Ingrese el costo de mano de obra por metro cuadrado: "))

area = altura * ancho

costo = area * monto_fijo

print(f"El costo para pintar la pared es de: ${costo}")
