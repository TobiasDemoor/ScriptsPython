from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from fisica import Entorno


class PuntosAnim:
    def __init__(self, dt: float = 1/30):
        self.dt = dt

    def initAnim(self):
        self.particles.set_data([], [])#, [])
        self.rect.set_edgecolor('none')
        self.rect2.set_edgecolor('none')
        return self.particles, self.rect, self.rect2

    def animate(self, i):
        self.entorno.step(self.dt)
        ms = int(self.fig.dpi * self.entorno.getSize())

        # update pieces of the animation
        self.rect.set_edgecolor('k')
        self.rect2.set_edgecolor('k')
        vect = self.entorno.state()
        vectX = []
        vectY = []
        # vectZ = []
        for q in vect:
            vectX.append(q[0])
            vectY.append(q[1])
            # vectZ.append(q[2])
        self.particles.set_data(vectX, vectY)#, vectZ)
        self.particles.set_markersize(ms)
        return self.particles, self.rect, self.rect2

    def main(self, entorno: Entorno):
        self.entorno = entorno
        # set up figure and animation
        self.fig = plt.figure(facecolor='black')
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.axes = self.fig.add_subplot(111, aspect='equal', autoscale_on=True,
                                       xlim=(-self.entorno.getMaxX(), self.entorno.getMaxX()),
                                       ylim=(-self.entorno.getMaxY(), self.entorno.getMaxY())
                                    )

        # particles holds the locations of the particles
        self.particles, = self.axes.plot([], [], 'bo', ms=6)

        # rect is the box edge
        self.rect = plt.Rectangle(self.entorno.getAncla(),
                                self.entorno.getAncho(),
                                self.entorno.getAlto(),
                                ec='none', lw=2, fc='none'
                                )
        self.rect2 = plt.Rectangle(
                                    (-self.entorno.getAncho()*self.entorno.rango/2,
                                    -self.entorno.getAlto()*self.entorno.rango/2),
                                self.entorno.getAncho()*self.entorno.rango,
                                self.entorno.getAlto()*self.entorno.rango,
                                ec='none', lw=2, fc='none'
                                )
        self.axes.add_patch(self.rect)
        self.axes.add_patch(self.rect2)
        # creo el objeto animacion
        self.anim = animation.FuncAnimation(
            self.fig, self.animate, init_func=self.initAnim, frames=600, interval=1000*self.dt, blit=True)
        plt.show()
