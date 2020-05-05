from fisica import *
from matPlotPoints import PuntosAnim


class Ave(Particula):
    __vision = 15
    __maxVel = 10
    __cercania = 5
    __factorReaccion = 6

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

    @staticmethod
    def setFactorReaccion(factorReaccion: float):
        Ave.__factorReaccion = factorReaccion

    @staticmethod
    def getFactorReaccion() -> float:
        return Ave.__factorReaccion

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

    def actualiza(self, aves: np.ndarray, dt: float):
        self.posFromVeldt(dt)
        prom = self.promedio(aves)
        tendPos = prom[0] - self.getPos()
        tendVel = self.getVel().prodVect(prom[1]).prodVect(self.getVel())
        tendCentro = self.getPos() * -1
        if tendPos.modulo() < Ave.getCercania():
            if tendPos.modulo() > 0:
                tendPos *= -1
            else:
                tendPos *= 0
        self.setTend(
            self.getTend().getUnitario() +
            tendVel.getUnitario() +
            tendPos.getUnitario() * 2+
            tendCentro.getUnitario()
        )
        self.setVel(self.getVel() + self.getTend() * Ave.getFactorReaccion() * dt)


class Jaula(Entorno):
    def __init__(self, ancho: float, alto: float, size: float = 7e-2, k: float = 1):
        super().__init__(ancho, alto, size, k)

    def generarAves(self, n: int, orden: float = 2):
        ancho = self.getAncho()
        alto = self.getAlto()
        maxX = self.getMaxX()
        maxY = self.getMaxY()
        for i in range(n):
            self.agregarParticula(Ave(
                ParOrdenado(np.random.rand()*ancho - maxX, np.random.rand()*alto - maxY),
                ParOrdenado((np.random.rand() * 2 * orden) - orden, (np.random.rand() * 2 * orden) - orden)
                ))


entorno = Jaula(20, 20)
entorno.generarAves(30, 10)
prueba = PuntosAnim(1/24)
prueba.main(entorno)
