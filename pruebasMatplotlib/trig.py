import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

class PuntoTrig:
    def __init__(self, theeta0):
        self.theeta0 = theeta0
        self.cos = math.cos(theeta0)
        self.sin = math.sin(theeta0)
    
    def getXY(self, i):
        val = math.sin(i+self.theeta0)
        return (self.cos*val, self.sin*val)

    def getSin(self):
        return self.sin
    
    def getCos(self):
        return self.cos

def initAnim():
    global particles, polinom
    particles.set_data([],[])
    polinom.set_data([],[])
    return particles, polinom

def animate(i):
    global particles, polinom, puntos
    vectX = []
    vectY = []
    for p in puntos:
        aux = p.getXY(i/12)
        vectX.append(aux[0])
        vectY.append(aux[1])
    particles.set_data(vectX, vectY)
    aux = puntos[0].getXY(i/12)
    vectX.append(aux[0])
    vectY.append(aux[1])
    polinom.set_data(vectX, vectY)
    polinom.set_data([],[])
    particles.set_markersize(5)
    return particles, polinom

puntos = []
n = 4
for i in range(n):
    puntos.append(PuntoTrig(i*math.pi/n))

# set up figure and animation
fig = plt.figure(facecolor='black')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
axes = fig.add_subplot(111, aspect='equal', autoscale_on=True,
                                xlim=(-2, 2),
                                ylim=(-2, 2)
                            )

# particles holds the locations of the particles
particles, = axes.plot([], [], 'bo', ms=6)
polinom, = axes.plot([],[],'b')
axes.add_artist(plt.Circle((0,0),1,fill=False))


for p in puntos:
    sin = p.getSin()
    cos = p.getCos()
    axes.plot([cos, -cos], [sin,-sin], color="black")


# creo el objeto animacion
anim = animation.FuncAnimation(
    fig, animate, init_func=initAnim, frames=1000, interval=42, blit=True)
plt.show()