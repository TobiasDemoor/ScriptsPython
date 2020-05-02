# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# creo la cuadrilla
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)


def init():
    # la inicializa
    line.set_data([], [])
    return line,


def animate(i):
    # arma cada frame
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


# creo el objeto animacion
anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=200, interval=20, blit=True)

# ffmpeg o mencoder para que funcione segun web
# anim.save('prueba.mp4', fps=30, extra_args=['-vcodec', 'libx246'])
plt.show()
