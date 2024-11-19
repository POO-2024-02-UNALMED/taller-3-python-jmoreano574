from __future__ import annotations
from televisores.marca import Marca 

class TV:
    _numTV = 0
    def __init__(self, marca : Marca, estado:bool)->None:
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        self._numTV += 1

    def estadoYmarca(self, marca, estado):
        if marca and estado == "encendido":
            return True
        else:
            return False
    #metodos setter 
    def setMarca(self,marca)->None:
        self._marca = marca 
    
    def setCanal(self, canal)->None:
        self._canal = canal

    def setPrecio(self, precio)->None:
        self._precio = precio

    def setVolumen(self, volumen)->None:
        self._volumen = volumen
    
    def setControl(self,control)->None:
        self._control = control

    #metodo getters
    def getMarca(self):
        return self._marca 
    
    def getCanal(self):
        return self._canal

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen
    
    def getControl(self):
        return self._control
    
    #metodo pára contar televisores
    def numTv(self, numTV)->None:
        self._numTV = numTV
    
    #metodo setter y getter metodo pára contar televisores
    def setnumTv(cls, numTV)->None:
        cls._numTV = numTV
    
    def getnumTv(cls):
        return cls._numTV
    
    #metodo para saber si esta encendido o apagado
    def turnOn(self) -> None:
        self._estado = True

    def turnOff(self) -> None:
        self._estado = False

     
    #metodo getter que retorna el atributo estado
    def getEstado(self,estado, marca):
        return self.estadoYmarca(estado,marca)
    
    #metodos para subir de canal y de el volumen
    def canalUp(self) -> None:
        self.setCanal(self._canal + 1)

    def canalDown(self) -> None:
        self.setCanal(self._canal - 1)

    
    def volumenUp(self) -> None:
        self.setVolumen(self._volumen + 1)
    
    def volumenDown(self)-> None:
        self.setVolumen(self._volumen - 1)
    
    #condicones para el estado
    def condiciones1(self, canal, estado)->None:
        if self.turnOn(estado) == "encendido" and self.canalUp(canal) >= 1 and self.canalUp(canal) <= 120 and self.canalDown(canal) <= 120 and self.canalDown(canal) >= 1:
            self._canal = canal 
        
    def condiciones2(self, volumen, estado)->None:
        if self.turnOn(estado) == "encendido" and self.volumenUp(volumen) >= 0 and self.volumenUp(volumen) <=7 and self.volumenDown(volumen) >= 0 and self.volumenDown(volumen):
            self._volumen = volumen
