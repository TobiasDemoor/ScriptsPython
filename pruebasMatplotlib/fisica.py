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
        return (pos - self)/self.distancia(pos)
    
    def getVect(self):
        return [self.getX(), self.getY(), self.getZ()]


class Particula:
    def __init__(self, masa: float, pos: ParOrdenado = ParOrdenado(), vel: ParOrdenado = ParOrdenado(), radio: float = 5e-6):
        self.__masa = masa
        self.__pos = pos
        self.__vel = vel
        self.__radio = radio

    def getMasa(self) -> float:
        return self.__masa

    def getPos(self) -> ParOrdenado:
        return self.__pos

    def getVel(self) -> ParOrdenado:
        return self.__vel

    def getRadio(self) -> float:
        return self.__radio

    def setPos(self, pos: ParOrdenado):
        self.__pos = pos

    def setVel(self, vel: ParOrdenado):
        self.__vel = vel

    def distancia(self, p) -> float:
        return self.getPos().distancia(p.getPos())

    def getVersor(self, p) -> ParOrdenado:
        return self.getPos().getVersor(p.getPos())

    def getVect(self):
        return self.getPos().getVect()


class ICampoVectorial:
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        pass


class CampoNulo:
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        return ParOrdenado()
