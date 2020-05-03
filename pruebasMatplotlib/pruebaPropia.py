import numpy as np
from parOrdenado import ParOrdenado
from matplotlib import pyplot as plt
from matplotlib import animation


class Carga:
    def __init__(self, carga: float, masa: float, x: float = 0, y: float = 0, velX: float = 0, velY: float = 0):
        self._carga = carga
        self._masa = masa
        self._pos = ParOrdenado(x, y)
        self._vel = ParOrdenado(velX, velY)

    def actualiza(self, cargas, dt: float):
        self._pos += self._vel * dt
        fuerza = ParOrdenado()
        for q in cargas:
            fuerza += q.getFuerza(self)
        acel = fuerza / self._masa
        self._vel += acel * dt

    def getPos(self) -> ParOrdenado:
        return self._pos

    def getCarga(self) -> float:
        return self._carga

    def distancia(self, q) -> float:
        return self._pos.distancia(q.getPos())

    def getVersor(self, q) -> ParOrdenado:
        return self._pos.getVersor(q.getPos())

    def getFuerza(self, q) -> ParOrdenado:
        dist = q.distancia(self)
        if (dist > 0):
            factor = 8.987e9*self._carga*q.getCarga()/dist
            res = self.getVersor(q) * factor
        else:
            res = ParOrdenado()
        return res
    
    def getVect(self):
        return [self.getPos().getX(), self.getPos().getY(), self._vel.getX(), self._vel.getY()]


class PruebaAnim:
    def __init__(self):
        self.__cargas = []

    def agregarCarga(self, carga: Carga):
        self.__cargas.append(carga)

    def step(self, dt):
        for q in self.__cargas:
            q.actualiza(self.__cargas, dt)
    
    def state(self):
        vect = []
        for q in self.__cargas:
            vect.append(q.getVect())
        return vect

    def initAnim(self):
        self.particles.set_data([], [])
        self.rect.set_edgecolor('none')
        return self.particles, self.rect

    def animate(self, i):
        self.step(self.dt)
        ms = int(self.fig.dpi * 2 * 0.1 * self.fig.get_figwidth()
                / np.diff(self.ax.get_xbound())[0])
        
        # update pieces of the animation
        self.rect.set_edgecolor('k')
        vect = self.state()
        vectX = []
        vectY = []
        print(vect)
        for q in vect :
            vectX.append(q[0])
            vectY.append(q[1])
        self.particles.set_data(vectX, vectY)
        self.particles.set_markersize(ms)
        return self.particles, self.rect

    def main(self):
        self.dt = 1/30
        # set up figure and animation
        self.fig = plt.figure()
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.ax = self.fig.add_subplot(111, aspect='equal', autoscale_on=False,
                             xlim=(-3.2, 3.2), ylim=(-2.4, 2.4))

        # particles holds the locations of the particles
        self.particles, = self.ax.plot([], [], 'bo', ms=6)

        # rect is the box edge
        self.rect = plt.Rectangle((-1, -1), 2, 2, ec='none', lw=2, fc='none')
        self.ax.add_patch(self.rect)
        # creo el objeto animacion
        self.anim = animation.FuncAnimation(
            self.fig, self.animate, init_func=self.initAnim, frames=600, interval=10, blit=True)
        plt.show()

prueba = PruebaAnim()
prueba.agregarCarga(Carga(1e-20,1e-30,-0.5,0,0,-0.3))
prueba.agregarCarga(Carga(-1e-20,1e-30,0.5,0,0,0.3))
prueba.main()