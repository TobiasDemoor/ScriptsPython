import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(10,200,20000)

hc = x*61.5*0.2/2
sc = 950*40.5/x
tc = hc + sc

ymin = np.min(tc)
xmin = x[list(tc).index(ymin)]

plt.vlines(xmin, -ymin, ymin, linestyles="dotted", label=xmin)
plt.plot(x, hc, label = "Costo de almacenamiento")
plt.plot(x, sc, label = "Costo de pedido")
plt.plot(x, tc, label = "Costo total")

plt.legend(loc='upper right')
plt.axis([10, 200, 0, np.max(tc)])
plt.show()