import numpy as np


class ParOrdenado:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        x = self.getX() + other.getX()
        y = self.getY() + other.getY()
        z = self.getZ() + other.getZ()
        return ParOrdenado(x, y, z)

    def __sub__(self, other):
        x = self.getX() - other.getX()
        y = self.getY() - other.getY()
        z = self.getZ() - other.getZ()
        return ParOrdenado(x, y, z)

    def __mul__(self, other):
        x = self.getX() * other
        y = self.getY() * other
        z = self.getZ() * other
        return ParOrdenado(x, y, z)

    def __truediv__(self, other):
        x = self.getX() / other
        y = self.getY() / other
        z = self.getZ() / other
        return ParOrdenado(x, y, z)

    def __floordiv__(self, other):
        x = self.getX() // other
        y = self.getY() // other
        z = self.getZ() // other
        return ParOrdenado(x, y, z)

    def __str__(self):
        return "(" + (str)(self.__x) + "," + (str)(self.__y) + "," + (str)(self.__z) + ")"

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def getZ(self) -> float:
        return self.__z

    def setX(self, x: float):
        self.__x = x

    def setY(self, y: float):
        self.__y = y

    def setZ(self, z: float):
        self.__z = z

    def prodEscalar(self, other) -> float:
        return self.getX() * other.getX() + self.getY() * other.getY() + self.getZ() * other.getZ()

    def prodVect(self, other):
        x = self.getY() * other.getZ() - self.getZ() * other.getY()
        y = self.getZ() * other.getX() - self.getX() * other.getZ()
        z = self.getX() * other.getY() - self.getY() * other.getX()
        return ParOrdenado(x, y, z)

    def modulo(self) -> float:
        return np.sqrt(self.getX() ** 2 + self.getY() ** 2 + self.getZ() ** 2)

    def distancia(self, pos) -> float:
        aux = self - pos
        return aux.modulo()

    def getVersor(self, pos):
        dist = self.distancia(pos)
        if (dist != 0):
            res = (pos - self)/dist
        else:
            res = ParOrdenado()
        return res

    def getUnitario(self):
        mod = self.modulo()
        if (mod > 0):
            res = self / self.modulo()
        else:
            res = ParOrdenado()
        return res

    def getArr(self):
        return [self.getX(), self.getY(), self.getZ()]


class Particula:
    def __init__(self, masa: float, pos: ParOrdenado, vel: ParOrdenado):
        self.__masa = masa
        self.__pos = pos
        self.__vel = vel

    def getMasa(self) -> float:
        return self.__masa

    def getPos(self) -> ParOrdenado:
        return self.__pos

    def getVel(self) -> ParOrdenado:
        return self.__vel

    def setPos(self, pos: ParOrdenado):
        self.__pos = pos

    def setVel(self, vel: ParOrdenado):
        self.__vel = vel

    def distancia(self, p) -> float:
        return self.getPos().distancia(p.getPos())

    def getVersor(self, p) -> ParOrdenado:
        return self.getPos().getVersor(p.getPos())

    def getArr(self):
        return self.getPos().getArr()
    
    def posFromVeldt(self, dt: float):
        self.__pos += self.__vel * dt

    def actualiza(self, particulas: np.ndarray, dt: float):
        raise NotImplementedError


class ICampoVectorial:
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        pass


class CampoNulo:
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        return ParOrdenado()

class CVConstante(ICampoVectorial):
    def __init__(self, x: float, y: float, z: float):
        self.__x = x
        self.__y = y
        self.__z = z 
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        return ParOrdenado(self.__x, self.__y, self.__z)

class Entorno:
    def __init__(self, ancho: float, alto: float, size: float, k: float):
        self.__ancho = ancho
        self.__alto = alto
        self.__ancla = (-ancho/2, -alto/2)
        self.__maxX = ancho/2 - size
        self.__maxY = alto/2 - size
        self.__size = size
        self.__k = k
        self.__particulas = []

    def getAncho(self) -> float:
        return self.__ancho

    def getAlto(self) -> float:
        return self.__alto

    def getAncla(self) -> tuple:
        return self.__ancla

    def getMaxX(self) -> float:
        return self.__maxX

    def getMaxY(self) -> float:
        return self.__maxY

    def getSize(self) -> float:
        return self.__size

    def getK(self) -> float:
        return self.__k
    
    def getParticulas(self) -> np.ndarray:
        return self.__particulas

    def setMaxX(self, maxX: float):
        self.__maxX = maxX

    def setMaxY(self, maxY: float):
        self.__maxY = maxY

    def agregarParticula(self, part: Particula):
        self.__particulas.append(part)
    
    def correccion(self, p: Particula):
        pos = p.getPos()
        vel = p.getVel()
        dx = 0
        dy = 0
        if (pos.getX() >= self.getMaxX()) or (pos.getX() <= -self.getMaxX()):
            dx = (pos.getX() - self.getMaxX())
            vel.setX(-self.getK() * abs(dx)/dx * abs(vel.getX()))
        if (pos.getY() >= self.getMaxY()) or (pos.getY() <= -self.getMaxY()):
            dy = (pos.getY() - self.getMaxY())
            vel.setY(-self.getK() * abs(dy)/dy * abs(vel.getY()))
        pos -= ParOrdenado(dx, dy)

    def step(self, dt: float):
        for p in self.__particulas:
            p.actualiza(self.__particulas, dt)
            self.correccion(p)

    def state(self) -> np.ndarray:
        vect = []
        for p in self.__particulas:
            vect.append(p.getArr())
        return vect
