from fisica import *
from matPlotPoints import PuntosAnim


class Ave(Particula):
    __vision = 3
    __maxVel = 8
    __cercania = 1

    @staticmethod
    def setVision(vision: float):
        Ave.__vision = vision

    @staticmethod
    def getVision() -> float:
        return Ave.__vision

    @staticmethod
    def setMaxVel(maxVel: float):
        Ave.__maxVel = maxVel

    @staticmethod
    def getMaxVel() -> float:
        return Ave.__maxVel

    @staticmethod
    def setCercania(cercania: float):
        Ave.__cercania = cercania

    @staticmethod
    def getCercania() -> float:
        return Ave.__cercania

    def __init__(self, pos: ParOrdenado = ParOrdenado(), vel: ParOrdenado = ParOrdenado()):
        super().__init__(1, pos, vel)
        self.__tendencia = ParOrdenado()

    def getTend(self) -> ParOrdenado:
        return self.__tendencia

    def setTend(self, tend: ParOrdenado):
        self.__tendencia = tend

    def setVel(self, vel: ParOrdenado):
        modulo = vel.modulo()
        if (modulo > Ave.getMaxVel()):
            vel *= Ave.getMaxVel() / modulo
        super().setVel(vel)

    def promedio(self, aves: np.ndarray) -> tuple:
        promPos = ParOrdenado()
        promVel = ParOrdenado()
        cont = 0
        for ave in aves:
            if self.distancia(ave) < Ave.getVision():
                promPos += ave.getPos()
                promVel += ave.getVel()
                cont += 1
        if cont != 0:
            promPos = promPos / cont
            promVel = promVel / cont
        else:
            promPos = self.getPos()
            promVel = self.getVel()
        return promPos, promVel

    def setVelPorTend(self, dt):
        tend = self.getTend()
        if (tend.modulo() > 0):
            self.setVel(self.getVel() + tend.prodVect(self.getVel()) * dt)

    def actualiza(self, aves: np.ndarray, dt: float):
        self.setPos(self.getPos() + self.getVel() * dt)
        prom = self.promedio(aves)
        vect = self.getPos().getVector(prom[0])
        tendCentro = self.getVel().prodVect(self.getPos() * -1)
        if vect.modulo() < Ave.getCercania():
            if vect.modulo() > 0:
                tendPos = self.getVel().prodVect(vect*-1)
            else:
                tendPos = ParOrdenado()
        else:
            tendPos = self.getVel().prodVect(vect)
        self.setTend((self.getTend() * 2+
                    self.getVel().prodVect(prom[1]) * 4 +
                    tendPos * 4 +
                    tendCentro
                    )/11)
        self.setVelPorTend(dt)


class Jaula(Entorno):
    def __init__(self, ancho: float, alto: float, size: float = 5e-2, k: float = 1):
        super().__init__(ancho, alto, size, k)

    def generarAves(self, n: int, orden: float = 2):
        for i in range(n):
            self.agregarParticula(Ave(
                ParOrdenado(np.random.rand()*self.getMaxX(), np.random.rand()*self.getMaxY()),
                ParOrdenado((np.random.rand()+0.5)*orden, (np.random.rand()+0.5)*orden)
                ))


entorno = Jaula(20, 20)
entorno.generarAves(20, 5)
prueba = PuntosAnim(1/24)
prueba.main(entorno)
