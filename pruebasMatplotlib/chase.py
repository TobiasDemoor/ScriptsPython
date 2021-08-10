import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math


class Dog:
    V = 0.01

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def setChased(self, chased):
        self.chased = chased

    def getNextXY(self):
        self.x += self.vx
        self.y += self.vy
        return (self.x, self.y)

    def getNexyVXVY(self):
        auxVX = self.chased.x - self.x
        auxVY = self.chased.y - self.y
        auxMod = math.sqrt(auxVX ** 2 + auxVY ** 2)
        self.vx = (auxVX / auxMod) * Dog.V
        self.vy = (auxVY / auxMod) * Dog.V


def initAnim():
    global particles, trails
    particles.set_data([], [])
    for trail in trails:
        trail.set_data([], [])
    return particles, *trails


def animate(i):
    global particles, trails, dogs, dogTrails
    vectX = []
    vectY = []
    for i, d in enumerate(dogs):
        aux = d.getNextXY()
        dogTrails[i][0].append(aux[0])
        dogTrails[i][1].append(aux[1])
        vectX.append(aux[0])
        vectY.append(aux[1])
    for d in dogs:
        d.getNexyVXVY()
    particles.set_data(vectX, vectY)
    for i, dt in enumerate(dogTrails):
        trails[i].set_data(dt[0], dt[1])
        trails[i].set_markersize(2)
    particles.set_markersize(5)
    return particles, *trails


dogs = [Dog(1, 1), Dog(1, -1), Dog(-1, -1), Dog(-1, 1)]
dogs[0].setChased(dogs[1])
dogs[1].setChased(dogs[2])
dogs[2].setChased(dogs[3])
dogs[3].setChased(dogs[0])

for d in dogs:
    d.getNexyVXVY()

# set up figure and animation
fig = plt.figure(facecolor='black')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
axes = fig.add_subplot(111, aspect='equal', autoscale_on=True,
                       xlim=(-2, 2),
                       ylim=(-2, 2)
                       )

# particles holds the locations of the particles
particles, = axes.plot([], [], 'bo', ms=6)
trails = []
dogTrails = []
for d in dogs:
    dogTrails.append(([], []))
    trail, = axes.plot([], [], 'b', ms=2)
    trails.append(trail)

# creo el objeto animacion
anim = animation.FuncAnimation(
    fig, animate, init_func=initAnim, frames=1000, interval=42, blit=True)
plt.show()
