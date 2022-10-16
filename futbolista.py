from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas=[]
    def _init_(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad=edad
    def getAltura(self):
        return self._altura
    def setAltura(self,altura):
        self._altura=altura
    def getSexo(self):
        return self._sexo
    def setSexo(self,sexo):
        self._sexo=sexo
    def getDeporte(self):
        return self._deporte
    def setDeporte(self,deporte):
        self._deporte=deporte
    def getAñosPracticando(self):
        return self._añosPracticando
    def setAñosPracticando(self,añosPracticando):
        self._añosPracticando=añosPracticando
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados=golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil=piernaHabil
    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas
    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls._listaFutbolistas=listaFutbolistas
    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"




    
