"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades), 
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. La promoción de 
jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

Para cada caso hacer:

● Una breve descripción de la situación comentada en la cabecera del archivo .py (similar a como hace Sergio en los ejemplos)

● Solución de pseudocódigo en PSeint

● Solución implementada en python en el mismo archivo donde se detalla la descripción"""

"""EPS
Entrada: Unidades(int), jubilado(str)
Proceso: Si lleva entre mas de 12 y 24 unidades se le hace un 10% de descuento 
         Si lleva mas de 24 unidades se le hace un 15% de descuento
         Siendo jubilado se le hace un 10% al total 
Salida: total(float)
"""

unidades = int(input("Cuantas unidades quieres llevar: "))
jubilado = input("Es jubilado: (si/no) ")
costo = 1000 * unidades
if unidades > 12 and unidades <= 24:
    total = costo - costo * 0.1
elif unidades > 24:
    total = costo - costo * 0.15
else:
    total = costo

if jubilado.lower() == "si":
    total = total - total * 0.10
    
print("El total es: ", total)






