import numpy as np
from parOrdenado import Pos, ParOrdenado


class Carga:
    def __init__(self, carga: float, masa: float, x: float = 0, y: float = 0, velX: float = 0, velY: float = 0):
        self._carga = carga
        self._masa = masa
        self._pos = Pos(x, y)
        self._vel = ParOrdenado(velX, velY)

    def actualiza(self, cargas, dt):
        self._pos += self._vel * dt
        fuerza = ParOrdenado()
        for q in cargas:
            fuerza += q.getFuerza(self)
        acel = fuerza * self._masa
        self._vel += acel * dt

    def getPos(self):
        return self._pos
    
    def getCarga(self):
        return self._carga
    
    def distancia(self, q: Carga) -> float:
        return self._pos.distancia(q.getPos())
    
    def getVersor(self, q: Carga) -> ParOrdenado:
        return self._pos.getVersor(q.getPos())

    def getFuerza(self, q: Carga) -> ParOrdenado:
        factor = 8.987e9*self._carga*q.getCarga()/q.distancia(self)
        return self.getVersor(q) * factor


class Prueba:
    def __init__(self):
        self._cargas = []
    
    
