class Monitor:
    contador_monitor = 0

    def __init__(self,marca,tamaño,id_monitor):
        Monitor.contador_monitor +=1
        self._marca = marca
        self._tamaño = tamaño
        self._id_monitor = Monitor.contador_monitor

    def __str__(self):
        return f"Monitor: {self._marca} , {self._tamaño} Pulgadas , ID:{self._id_monitor}"

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self,tamaño):
        self._tamaño = tamaño

if __name__ == "__main__":
    monitor1 = Monitor("KANJI", 15,Monitor.contador_monitor)
    print(monitor1)
    monitor2 = Monitor("HP", 24, Monitor.contador_monitor)
    print(monitor2)