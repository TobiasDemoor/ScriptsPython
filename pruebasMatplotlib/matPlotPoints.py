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
        # vectZ = []
        for q in vect:
            vectX.append(q[0])
            vectY.append(q[1])
            # vectZ.append(q[2])
        self.particles.set_data(vectX, vectY)#, vectZ)
        self.particles.set_markersize(ms)
        return self.particles, self.rect

    def main(self, entorno: Entorno):
        self.entorno = entorno
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
            self.fig, self.animate, init_func=self.initAnim, frames=600, interval=5, blit=True)
        plt.show()
