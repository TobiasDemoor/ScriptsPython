import numpy as np
from fisica import ParOrdenado, Particula, Entorno

from matplotlib import pyplot as plt
from matplotlib import animation

import threading

class PuntosAnim:
    def __init__(self, entorno,  dt: float = 1/30):
        self.entorno = entorno
        self.dt = dt
        self.entorno.setDt(self.dt)

    def initAnim(self):
        self.particles.set_data([], [])#, [])
        self.rect.set_edgecolor('none')
        self.rect2.set_edgecolor('none')
        return self.particles, self.rect, self.rect2

    def animate(self, i):
        ms = int(self.fig.dpi * self.entorno.getSize())

        # update pieces of the animation
        self.rect.set_edgecolor('k')
        self.rect2.set_edgecolor('k')
        vect = self.entorno.getStep()
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

    def main(self):
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



class Ave(Particula):
    __vision = 20
    __maxVel = 20
    __cercania = 2
    __factorReaccion = 1

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

    def promedio(self, aves: np.array) -> tuple:
        centro = ParOrdenado()
        promVel = ParOrdenado()
        repulsion = ParOrdenado()
        miPos = self.getPos()
        cont = 0
        for ave in aves:
            dist = self.distancia(ave)
            if dist < Ave.getVision():
                pos = ave.getPos()
                if dist < Ave.getCercania():
                    repulsion += miPos - pos
                centro += pos
                promVel += ave.getVel()
                cont += 1
        if cont != 0:
            centro /= cont
            promVel /= cont
        else:
            centro = self.getPos()
            promVel = self.getVel()
        return centro, promVel, repulsion

    def actualiza(self, aves: np.array, dt: float):
        self.setPos(self.getPos() + self.getVel() * dt)
        prom = self.promedio(aves)
        tendPos = prom[0] - self.getPos()
        tendVel = prom[1] - self.getVel()
        # if tendPos.modulo() < Ave.getCercania():
        #     if tendPos.modulo() > 0:
        #         tendPos *= -1
        #     else:
        #         tendPos *= 0
        # print(tendPos)
        self.setVel(self.getVel() + (tendVel * dt + tendPos + prom[2]).getUnitario() * Ave.getFactorReaccion())
        # self.setTend(
        #     self.getTend() * 2 +
        #     (tendVel + tendPos) / 2
        # )
        # self.setVel(self.getVel() + (self.getTend() + (tendVel + tendPos) * 2) * Ave.getFactorReaccion() * dt)


class Jaula(Entorno):
    MAX_BUFFER = 10

    def __init__(self, ancho: float, alto: float, size: float = 5e-2, rango: float = 0.8, k: float = 1):
        super().__init__(ancho, alto, size, k)
        if ancho > alto:
            self.radioAtr = alto/2
        else:
            self.radioAtr = ancho/2
        self.radioAtr *= rango
        self.rango = rango
        self.lock = threading.Lock()
        self.semBufferOut = threading.Semaphore(0)
        self.semBufferIn = threading.Semaphore(Jaula.MAX_BUFFER)
        self.buffer = []

    def correccion(self, p: Ave):
        pos = p.getPos()
        if pos.modulo() > self.radioAtr:
            p.setVel(p.getVel() - p.getPos())
        super().correccion(p)
    
    def setDt(self, dt: float):
        self.dt = dt

    def getStep(self):
        self.semBufferOut.acquire()
        self.lock.acquire()
        result = self.buffer.pop(0)
        print(len(self.buffer))
        self.lock.release()
        self.semBufferIn.release()
        return result

    def genStep(self):
        self.semBufferIn.acquire()
        for p in self.getParticulas():
            self.correccion(p)
            p.actualiza(self.getParticulas(), self.dt)
        self.lock.acquire()
        self.buffer.append(map(lambda par: par.getArr(), self.getParticulas()))
        print(len(self.buffer))
        self.lock.release()
        self.semBufferOut.release()

    def generarAves(self, n: int, orden: float = 2):
        ancho = self.getAncho() * self.rango
        alto = self.getAlto() * self.rango
        maxX = self.getAncho()/2 * self.rango
        maxY = self.getAlto()/2 * self.rango
        for i in range(n):
            i = i # no me rompas las bolas pylint
            self.agregarParticula(Ave(
                ParOrdenado(np.random.rand()*ancho - maxX, np.random.rand()*alto - maxY),
                ParOrdenado((np.random.rand() * 2 * orden) - orden, (np.random.rand() * 2 * orden) - orden)
                ))

def generate(entorno: Jaula):
    while True:
        entorno.genStep()

entorno = Jaula(20, 20)
entorno.generarAves(20, 100)
prueba = PuntosAnim(entorno, 1/60)
threading.Thread(target= generate, args=(entorno,)).start()
prueba.main()