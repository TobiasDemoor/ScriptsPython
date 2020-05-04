from fisica import *
from matPlotPoints import PuntosAnim


class Carga(Particula):
    def __init__(self, carga: float, masa: float, pos: ParOrdenado = ParOrdenado(), vel: ParOrdenado = ParOrdenado(), radio: float = 5e-6):
        super().__init__(masa, pos, vel, radio)
        self.__carga = carga

    def getCarga(self) -> float:
        return self.__carga

    def _fuerzaCoulombQ(self, cargas: np.ndarray) -> ParOrdenado:
        fuerza = ParOrdenado()
        for q in cargas:
            fuerza += q.getFuerza(self)
        return fuerza

    def _fuerzaCoulombE(self, e: ICampoVectorial) -> ParOrdenado:
        return e.valor(self.getPos()) * self.getCarga()

    def _fuerzaLorentz(self, b: ICampoVectorial) -> ParOrdenado:
        return self.getVel().prodVect(b.valor(self.getPos())) * self.getCarga()

    def _fuerzaTotal(self, cargas: np.ndarray, e: ICampoVectorial, b: ICampoVectorial):
        return self._fuerzaCoulombQ(cargas) + self._fuerzaCoulombE(e) + self._fuerzaLorentz(b)

    def actualiza(self, cargas: np.ndarray, dt: float, e: ICampoVectorial = CampoNulo(), b: ICampoVectorial = CampoNulo()):
        self.setPos(self.getPos() + self.getVel() * dt)
        self.setVel(self.getVel() +
                    (self._fuerzaTotal(cargas, e, b) / self.getMasa()) * dt)

    def getFuerza(self, q) -> ParOrdenado:
        dist = q.distancia(self)
        if (dist > self.getRadio()):
            res = self.getVersor(
                q) * (8.987e9 * self.getCarga() * q.getCarga() / dist ** 2)
        elif (dist > 0):
            # placeholder de repulsion cercana
            res = self.getVersor(q) * abs(8.987e9 *
                                          self.getCarga() * q.getCarga())
        else:
            res = ParOrdenado()
        return res


class CargaInamovible(Carga):
    def _fuerzaTotal(self, cargas, e, b) -> ParOrdenado:
        return ParOrdenado()


class EntornoCCampo(Entorno):
    def __init__(self, ancho: float, alto: float, size: float = 0.04, k: float = 0.9, e: ICampoVectorial = CampoNulo(), b: ICampoVectorial = CampoNulo()):
        super().__init__(ancho, alto, size, k)
        self.__e = e
        self.__b = b
    
    def step(self, dt: float):
        for q in self.getParticulas():
            q.actualiza(self.getParticulas(), dt, self.__e, self.__b)
            self.correccion(q)

entorno = EntornoCCampo(4, 4, k=0.8, b=CVConstante(0, 0, 1e-9))
# entorno.agregarParticula(
#     Carga(-1e-20, 2e-30, ParOrdenado(-0.5, 0), ParOrdenado(0, 0.3)))
entorno.agregarParticula(
    Carga(-1e-20, 2e-30, ParOrdenado(0.5, 0), ParOrdenado(0, -0.3)))
# entorno.agregarParticula(
#     Carga(-1e-20, 2e-30, ParOrdenado(0, -0.5), ParOrdenado(-0.3, 0)))
entorno.agregarParticula(
    Carga(-1e-20, 2e-30, ParOrdenado(0, 0.5), ParOrdenado(0.3, 0)))
# entorno.agregarParticula(CargaInamovible(1e-20, 1))
prueba = PuntosAnim()
prueba.main(entorno)
