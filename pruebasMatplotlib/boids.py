from fisica import *
from matPlotPoints import PuntosAnim


class Ave(Particula):
    __vision = 10
    __maxVel = 10
    __cercania = 0.1

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

    def __init__(self, masa: float, pos: ParOrdenado = ParOrdenado(), vel: ParOrdenado = ParOrdenado(), radio: float = 5e-6):
        super().__init__(masa, pos, vel, radio)

    def promedioVel(self, aves: np.ndarray) -> ParOrdenado:
        promVel = ParOrdenado()
        cont = 0
        for ave in aves:
            if self.distancia(ave) < Ave.getVision():
                promVel += ave.getVel()
                cont += 1
        promVel /= cont  # no deberia causar problemas porque estoy incluido en aves
        return promVel
    
    def promedioPos(self, aves: np.ndarray) -> ParOrdenado:
        promPos = ParOrdenado()
        cont = 0
        for ave in aves:
            if self.distancia(ave) < Ave.getVision():
                promPos += ave.getPos()
                cont += 1
        promPos /= cont  # no deberia causar problemas porque estoy incluido en aves
        return promPos
    
    def setVel(self, vel: ParOrdenado):
        modulo = vel.modulo()
        if (modulo > Ave.getMaxVel()):
            vel *= Ave.getMaxVel() / modulo
        super().setVel(vel)

    def actualiza(self, aves: np.ndarray, dt: float):
        # promPos = self.promedioPos(aves)
        promVel = self.promedioVel(aves)
        self.setPos(self.getPos() + self.getVel() * dt)
        self.setVel((promVel) * self.getVel().modulo()/(promVel.modulo()))
        # if self.distancia(promPos) < Ave.getCercania():
        #     pass
        
class Jaula(Entorno):
    def __init__(self, ancho: float, alto: float, size: float = 0.1, k: float = 1):
        super().__init__(ancho, alto, size, k)
    
entorno = Jaula(10, 10)
entorno.agregarParticula(Ave(1, ParOrdenado(1,1), ParOrdenado(0, 1)))
entorno.agregarParticula(Ave(1, ParOrdenado(1, -1), ParOrdenado(1, 1)))
entorno.agregarParticula(Ave(1, ParOrdenado(-1, -1), ParOrdenado(1, -1)))
entorno.agregarParticula(Ave(1, ParOrdenado(-1, 1), ParOrdenado(0, -1)))
prueba = PuntosAnim()
prueba.main(entorno)