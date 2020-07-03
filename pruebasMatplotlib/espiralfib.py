from matplotlib import patches
import matplotlib.pyplot as plt
import math


tope = 11
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')


centro = [0, 0]
angulo = 90
a = 0
b = 1
c = 1
for i in range(1, tope):
    d = 2*b
    ax.add_patch(
        patches.Arc(tuple(centro), d, d, angle=angulo, theta2=90)
    )
    angulo -= 90
    if angulo % 180 == 0:
        centro[1] -= math.cos(math.radians(angulo))*a
    else:
        centro[0] += math.sin(math.radians(angulo))*a
    a, b, c = b, c, b+c

tup = (-b*1.1, b*1.1)
ax.set(xlim=tup, ylim=tup)
plt.show()
