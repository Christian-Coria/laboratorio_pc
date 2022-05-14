from clase_computadora import Computadora


class Orden:
    contador_ordenes = 0

    def __init__(self,computadoras,id_orden):
        Orden.contador_ordenes +=1
        self._id_ordenes = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self,computadora):
        self._computadoras.append(computadora)
    

    def __str__(self):
        #creamos una variable (cadena vacia) en plural ya que almacenara todos los objetos de tipo computadora
        computadoras_str = ""
        #recorremos toda la lista de computadoras almacenando en la variable computadora cada objeto
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f"""
        Orden: {self._id_ordenes} 
        {computadoras_str}

        """
    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadora(self,computadoras):
        self._computadoras = computadoras


