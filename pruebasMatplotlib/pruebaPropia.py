import numpy as np
from parOrdenado import ParOrdenado
from matplotlib import pyplot as plt
from matplotlib import animation


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
        return [self.getPos().getX(), self.getPos().getY()]


class ICampoVectorial:
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        pass


class CampoNulo:
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        return ParOrdenado


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
        return ParOrdenado()

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
            res = self.getVersor(q) * abs(8.987e9 *
                                          self.getCarga() * q.getCarga())
        else:
            res = ParOrdenado()
        return res


class CargaInamovible(Carga):
    def _fuerzaTotal(self, cargas, e, b) -> ParOrdenado:
        return ParOrdenado()


class Entorno:
    def __init__(self, ancho: float, alto: float, size: float = 0.04, k: float = 0.9, e: ICampoVectorial = CampoNulo(), b: ICampoVectorial = CampoNulo()):
        self.__ancho = ancho
        self.__alto = alto
        self.__ancla = (-ancho/2, -alto/2)
        self.__maxX = ancho/2 - size
        self.__maxY = alto/2 - size
        self.__size = size
        self.__k = k
        self.__e = e
        self.__b = b
        self.__cargas = []

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

    def agregarCarga(self, carga: Carga):
        self.__cargas.append(carga)

    def step(self, dt: float):
        for q in self.__cargas:
            q.actualiza(self.__cargas, dt, self.__e, self.__b)
            pos = q.getPos()
            vel = q.getVel()
            dx = 0
            dy = 0
            if (pos.getX() >= self.getMaxX()) or (pos.getX() <= -self.getMaxX()):
                dx = (pos.getX() - self.getMaxX())
                vel.setX(-self.getK() * abs(dx)/dx * abs(vel.getX()))
            if (pos.getY() >= self.getMaxY()) or (pos.getY() <= -self.getMaxY()):
                dy = (pos.getY() - self.getMaxY())
                vel.setY(-self.getK() * abs(dy)/dy * abs(vel.getY()))
            pos -= ParOrdenado(dx, dy)

    def state(self) -> np.ndarray:
        vect = []
        for q in self.__cargas:
            vect.append(q.getVect())
        return vect


class PruebaAnim:
    def initAnim(self):
        self.particles.set_data([], [])
        self.rect.set_edgecolor('none')
        return self.particles, self.rect

    def animate(self, i):
        self.entorno.step(self.dt)
        ms = int(self.fig.dpi * 2 * self.entorno.getSize() * self.fig.get_figwidth()
                 / np.diff(self.ax.get_xbound())[0])

        # update pieces of the animation
        self.rect.set_edgecolor('k')
        vect = self.entorno.state()
        vectX = []
        vectY = []
        for q in vect:
            vectX.append(q[0])
            vectY.append(q[1])
        self.particles.set_data(vectX, vectY)
        self.particles.set_markersize(ms)
        return self.particles, self.rect

    def main(self, entorno: Entorno):
        self.entorno = entorno
        self.dt = 1/30
        # set up figure and animation
        self.fig = plt.figure()
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.ax = self.fig.add_subplot(111, aspect='equal', autoscale_on=False,
                                       xlim=(-self.entorno.getMaxX(), self.entorno.getMaxX()), ylim=(-self.entorno.getMaxY(), self.entorno.getMaxY()))

        # particles holds the locations of the particles
        self.particles, = self.ax.plot([], [], 'bo', ms=6)

        # rect is the box edge
        self.rect = plt.Rectangle(self.entorno.getAncla(), self.entorno.getAncho(
        ), self.entorno.getAlto(), ec='none', lw=2, fc='none')
        self.ax.add_patch(self.rect)
        # creo el objeto animacion
        self.anim = animation.FuncAnimation(
            self.fig, self.animate, init_func=self.initAnim, frames=600, interval=10, blit=True)
        plt.show()


class EConstante(ICampoVectorial):
    def valor(self, punto: ParOrdenado) -> ParOrdenado:
        return ParOrdenado(0, 1e-9)


entorno = Entorno(10, 8, e=EConstante())
entorno.agregarCarga(
    Carga(-1e-20, 2e-30, ParOrdenado(-0.5, 0), ParOrdenado(0, 0.3)))
entorno.agregarCarga(
    Carga(-1e-20, 2e-30, ParOrdenado(0.5, 0), ParOrdenado(0, -0.3)))
entorno.agregarCarga(
    Carga(-1e-20, 2e-30, ParOrdenado(0, -0.5), ParOrdenado(-0.3, 0)))
entorno.agregarCarga(
    Carga(-1e-20, 2e-30, ParOrdenado(0, 0.5), ParOrdenado(0.3, 0)))
entorno.agregarCarga(CargaInamovible(1e-20, 1))
prueba = PruebaAnim()
prueba.main(entorno)
