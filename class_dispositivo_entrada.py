
class Dispositivo_entrada:

    def __init__(self,tipo_entrada,marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def __str__(self):
        return f"Tipo de Entrada: {self._tipo_entrada} , Marca: {self._marca}"

    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
    @tipo_entrada.setter
    def tipo_entrada(self,tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca

if __name__ == "__main__":
     dispositivo1 = Dispositivo_entrada("USB","KANJI")
     print(dispositivo1)
    


