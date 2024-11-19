class TV:
    _numTV = 0
    def __init__(self, marca : Marca, canal:int, precio:int, estado:bool, volumen:int, control: Control):
        self._marca = marca
        self._canal = canal
        self._precio = precio
        self._estado = estado
        self._volumen = volumen
        self._control = control
        self._numTV += 1

    def estadoYmarca(self, marca, estado):
        if marca and estado == "encendido":
            return True
        else:
            return False
    #metodos setter 
    def setMarca(self,marca):
        self._marca = marca 
    
    def setCanal(self):
        self._canal = 1

    def setPrecio(self):
        self._precio = 500

    def setVolumen(self):
        self._volumen = 1
    
    def setControl(self,control):
        self._control = control

    #metodo getters
    def getMarca(self):
        return self.marca 
    
    def getCanal(self):
        return self.canal

    def getPrecio(self):
        return self.precio

    def getVolumen(self):
        return self.volumen
    
    def getControl(self):
        return self.control
    
    #metodo pára contar televisores
    def numTv(self, numTV):
        self._numTV = numTV
    
    #metodo setter y getter metodo pára contar televisores
    def setnumTv(self, numTV):
        self._numTV = numTV
    
    def getnumTv(self):
        return self._numTV
    
    #metodo para saber si esta encendido o apagado
    def turnOn(self, estado):
        self.estadoYmarca(estado)
    
    def turnOff(self, estado):
        self.estadoYmarca(estado)
     
    #metodo getter que retorna el atributo estado
    def getEstado(self,estado):
        return self.estadoYmarca(estado)
    
    #metodos para subir de canal y de el volumen
    def canalUp(self, canal):
        self.setCanal(canal + 1)
    
    def canalDonw(self, canal):
        self.setCanal(canal - 1)
    
    def volumenUp(self, volumen):
        self.setVolumen(volumen + 1)
    
    def volumenDown(self, volumen):
        self.setVolumen(volumen - 1)
    
    #condicones para el estado
    def condiciones1(self, canal, estado):
        if self.turnOn(estado) == "encendido" and self.canalUp(canal) >= 1 and self.canalUp(canal) <= 120 and self.canalDown(canal) <= 120 and self.canalDown(canal) >= 1:
            self._canal = canal 
        
    def condiciones2(self, volumen, estado):
        if self.turnOn(estado) == "encendido" and self.volumenUp(volumen) >= 0 and self.volumenUp(volumen) <=7 and self.volumenDown(volumen) >= 0 and self.volumenDown(volumen):
            self._volumen = volumen
