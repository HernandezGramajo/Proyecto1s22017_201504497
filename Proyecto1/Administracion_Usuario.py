
class Nodo:
    def __init__(self,datos):
        self.siguiente = None
        self.anterior = None
        self.info = datos

    def VerNodo(self):
        return  self.info

class Listadoble:

    def  __init__(self):
        self.cabeza = None
        self.Cola = None

    def vacia (self):
        if self.cabeza == None:
            return  True
        else :
            return  False

    def insertarPrimero(self,datos):
        temporal = Nodo(datos)
        if self.vacia() == True:
            self.cabeza = temporal
            self.cola = temporal 



