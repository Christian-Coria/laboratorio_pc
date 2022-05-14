from class_dispositivo_entrada import Dispositivo_entrada


class Teclado(Dispositivo_entrada):
    contador_teclado = 0

    def __init__(self,tipo_entrada,marca,id_teclado):
        Teclado.contador_teclado += 1
        super().__init__(tipo_entrada,marca) 
        self._id_teclado = Teclado.contador_teclado

    def __str__(self) :
        return f"TECLADO: {super().__str__()}, ID: {self._id_teclado}"

if __name__ == "__main__":
    teclado1 = Teclado("usb", "Kanji",Teclado.contador_teclado)
    print(teclado1)
