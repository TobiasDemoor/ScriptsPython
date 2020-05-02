import numpy as np


class ParOrdenado:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def getX(self) -> float:
        return self._x

    def getY(self) -> float:
        return self._y

    def setX(self, x: float):
        self._x = x

    def setY(self, y: float):
        self._y = y

    def incr(self, incr: ParOrdenado):
        self._x += incr.getX()
        self._y += incr.getY()

    def actualiza(self, par: ParOrdenado, dt: float):
        par.setX(par.getX() + self._x * dt)
        par.setY(par.getY() + self._y * dt)
    
    def ampliar(self, factor: float):
        self._x *= factor
        self._y *= factor


class Pos(ParOrdenado):
    def __init__(self, x: float, y: float):
        super(x, y)

    def distancia(self, pos: Pos) -> float:
        return np.sqrt((self._x - pos.getX())**2 + (self._y - pos.getY())**2)
    
    def getVersor(self, pos: Pos) -> ParOrdenado:
        modulo = self.distancia(pos)
        x = pos.getX() - self._x
        y = pos.getY() - self._y
        x /= modulo
        y /= modulo
        return Pos(x, y)


class Vel(ParOrdenado):
    def __init__(self, x: float, y: float):
        super(x, y)

    def actualiza(self, pos: Pos, dt: float):
        super.actualiza(pos, dt)


class Acel(ParOrdenado):
    def __init__(self, x: float, y: float):
        super(x, y)

    def actualiza(self, vel: Vel, dt: float):
        super.actualiza(vel, dt)


class Fuerza(ParOrdenado):
    def __init__(self, x: float = 0, y: float = 0):
        super(x, y)

    def getAcel(self, masa: float) -> Acel:
        return Acel(self._x*masa, self._y*masa)


class Carga:
    def __init__(self, carga: float, masa: float, x: float = 0, y: float = 0, velX: float = 0, velY: float = 0):
        self._carga = carga
        self._masa = masa
        self._pos = Pos(x, y)
        self._vel = Vel(velX, velY)

    def actualiza(self, cargas, dt):
        self._vel.actualiza(self._pos, dt)
        fuerza = Fuerza()
        for q in cargas:
            fuerza.incr(q.getFuerza(self))
        acel = fuerza.getAcel(self._masa)
        acel.actualiza(self._vel, dt)

    def getPos(self):
        return self._pos
    
    def getCarga(self):
        return self._carga
    
    def distancia(self, q: Carga) -> float:
        return self._pos.distancia(q.getPos())
    
    def getVersor(self, q: Carga) -> ParOrdenado:
        return self._pos.getVersor(q.getPos())

    def getFuerza(self, q: Carga) -> Fuerza:
        factor = 8.987e9*self._carga*q.getCarga()/q.distancia(self)
        versor = self.getVersor(q)
        versor.ampliar(factor)
        return Fuerza(versor.getX(), versor.getY())


class Prueba:
    def __init__(self):
        self._cargas = []
    
    
