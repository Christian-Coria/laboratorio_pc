from class_dispositivo_entrada import Dispositivo_entrada


class Raton(Dispositivo_entrada):
    contador_raton = 0

    def __init__(self, tipo_entrada, marca,id_raton):
        Raton.contador_raton += 1
        super().__init__(tipo_entrada, marca)
        self._id_raton = Raton.contador_raton

    def __str__(self):
        return f"MOUSE: {super().__str__()}, ID: {self._id_raton} "

if __name__ == "__main__":
    raton1 = Raton("USB", "kanji",Raton.contador_raton)
    print(raton1)