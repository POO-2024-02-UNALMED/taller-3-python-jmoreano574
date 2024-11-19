from __future__ import annotations
from televisores.tv import TV

class Control:
    def __init__(self)->None:
        self._tv = None 
    
    def enlazar(self, tv)->None:
        self._tv = tv
        tv.setControl(self)

    def turnOn(self,estado:bool)->None:
        self._tv.turnOn(estado)

    def turnOff(self,estado:bool)->None:
        self._tv.turnOff(estado)

    def canalUp(self,canal: int)->None:
        self._tv.canalUp(canal)
    
    def canalDown(self,canal:int)->None:
        self._tv.canalDown()

    def volumenUp(self,volumen:int)->None:
        self._tv.volumenUp()

    def volumenDown(self,volumen: int)->None:
        self._tv.volumenDown(volumen)

    def setCanal(self, canal: int)->None:
        self._tv.setCanal(canal)

    def setVolumen(self, volumen: int)->None:
        self._tv.setVolumen(volumen)

    def getTv(self):
        return self._tv
    
    def setTv(self, tv:TV)->None:
        self._tv = tv
