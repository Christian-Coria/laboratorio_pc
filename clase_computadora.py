from class_raton import Raton
from class_monitor import Monitor
from class_teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self,nombre,monitor,raton,teclado,id_computadora):
        Computadora.contador_computadora +=1
        self._id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self._monitor = monitor
        self._raton = raton
        self._teclado = teclado

    def __str__(self):
        return f"""
        {self.nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Mouse: {self._raton}
        Teclado: {self._teclado}
        """

#agregamos los objetos teclado, raton,monitor por Agregacion importando las clases
teclaco1 = Teclado("usb","kanji",Teclado.contador_teclado)
raton1 = Raton("usb","hp",Raton.contador_raton)
monitor1 = Monitor("hp", 15, Monitor.contador_monitor)
computadora1 = Computadora("HP",monitor1,raton1,teclaco1,Computadora.contador_computadora)
print(computadora1)

teclaco2 = Teclado("Bluethoot","Sony",Teclado.contador_teclado)
raton2 = Raton("Bluethoot","hp",Raton.contador_raton)
monitor2 = Monitor("Sony", 15, Monitor.contador_monitor)
computadora2 = Computadora("Sony",monitor1,raton1,teclaco1,Computadora.contador_computadora)
print(computadora2)

teclaco3 = Teclado("usb","xiaomi",Teclado.contador_teclado)
raton3 = Raton("usb","xiaomi",Raton.contador_raton)
monitor3 = Monitor("xiaomi", 15, Monitor.contador_monitor)
computadora3 = Computadora("xiaomi",monitor1,raton1,teclaco1,Computadora.contador_computadora)
print(computadora3)