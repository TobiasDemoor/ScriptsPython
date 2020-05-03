import numpy as np


class ParOrdenado:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.__x = x
        self.__y = y
        self.__z = z

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

    def modulo(self) -> float:
        aux = self ** 2
        return np.sqrt(aux.getX()+aux.getY()+aux.getZ())

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

    def __div__(self, other):
        x = self.getX() / other
        y = self.getY() / other
        z = self.getZ() / other
        return ParOrdenado(x, y, z)
    
    def __pow__(self, other):
        x = self.getX() ** other
        y = self.getY() ** other
        z = self.getZ() ** other
        return ParOrdenado(x, y, z)

    def __str__(self):
        return "(" + (str)(self.__x) + "," + (str)(self.__y) + "," + (str)(self.__z) + ")"


class Pos(ParOrdenado):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        super(x, y, z)

    def distancia(self, pos: ParOrdenado) -> float:
        aux = self - pos
        return aux.modulo()

    def getVersor(self, pos: ParOrdenado) -> ParOrdenado:
        return (pos - self)/self.distancia(pos)


p1 = ParOrdenado(1, 1)
p2 = ParOrdenado(0, 0)
print(p1-p2)
