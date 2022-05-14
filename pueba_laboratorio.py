from clase_computadora import Computadora
from class_monitor import Monitor
from class_orden import Orden
from class_raton import Raton
from class_teclado import Teclado



teclaco1 = Teclado("usb","kanji",Teclado.contador_teclado)
raton1 = Raton("usb","hp",Raton.contador_raton)
monitor1 = Monitor("hp", 15, Monitor.contador_monitor)
computadora1 = Computadora("HP",monitor1,raton1,teclaco1,Computadora.contador_computadora)


teclaco2 = Teclado("Bluethoot","Sony",Teclado.contador_teclado)
raton2 = Raton("Bluethoot","hp",Raton.contador_raton)
monitor2 = Monitor("Sony", 15, Monitor.contador_monitor)
computadora2 = Computadora("Sony",monitor1,raton1,teclaco1,Computadora.contador_computadora)



teclaco3 = Teclado("usb","xiaomi",Teclado.contador_teclado)
raton3 = Raton("usb","xiaomi",Raton.contador_raton)
monitor3 = Monitor("xiaomi", 15, Monitor.contador_monitor)
computadora3 = Computadora("xiaomi",monitor1,raton1,teclaco1,Computadora.contador_computadora)

#creamos una lista de computadoras
computadoras1 = [computadora1,computadora2]
computadoras2 = [computadora3]

#CREAMOS EL OBJETO DE ORDEN

orden1 = Orden(computadoras1,Orden.contador_ordenes)
print(orden1)
orden2 = Orden(computadoras2,Orden.contador_ordenes)
print(orden2)