from __future__ import annotations
from televisores.marca import Marca
from televisores.control import Control

class TV:
    _numTV = 0

    def __init__(self, marca: Marca, estado: bool):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1  # Uso de la clase para incrementar el contador

    # Métodos setters
    def setMarca(self, marca: Marca):
        self._marca = marca

    def setCanal(self, canal: int):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    def setPrecio(self, precio: int):
        self._precio = precio

    def setVolumen(self, volumen: int):
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    def setControl(self, control: Control):
        self._control = control

    # Métodos getters
    def getMarca(self) -> Marca:
        return self._marca

    def getCanal(self) -> int:
        return self._canal

    def getPrecio(self) -> int:
        return self._precio

    def getVolumen(self) -> int:
        return self._volumen

    def getControl(self):
        return self._control

    # Métodos para encender y apagar el televisor
    def turnOn(self) -> None:
        self._estado = True

    def turnOff(self) -> None:
        self._estado = False

    def getEstado(self) -> bool:
        return self._estado

    # Métodos para cambiar de canal y volumen
    def canalUp(self) -> None:
        if self._estado and self._canal < 120:
            self._canal += 1

    def canalDown(self) -> None:
        if self._estado and self._canal > 1:
            self._canal -= 1

    def volumenUp(self) -> None:
        if self._estado and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self) -> None:
        if self._estado and self._volumen > 0:
            self._volumen -= 1

    # Método para obtener el número de televisores
    @classmethod
    def getNumTV(cls):
        return cls._numTV

    # Métodos para condiciones (ajustados)
    def condiciones1(self, canal):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    def condiciones2(self, volumen):
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    # Métodos para establecer y obtener el número de televisores 
    def setNumTV(cls, numTV: int):
        cls._numTV = numTV
