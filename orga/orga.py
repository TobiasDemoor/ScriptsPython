import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(10,200,1000000)

hc = x*61.5*0.2/2
sc = 950*40.5/x
tc = hc + sc

ymin = np.min(tc)
xmin = x[list(tc).index(ymin)]

plt.hlines(ymin, 10, xmin, linestyles="dotted", label="Costo mínimo = $%.2f"%(ymin+0.01))
plt.vlines(xmin, 0, ymin, linestyles="dotted", label="EOQ = %.3f unidades"%xmin)
plt.plot(x, hc, label = "Costo de almacenamiento (QCi/2)")
plt.plot(x, sc, label = "Costo de pedido (DS/Q)")
plt.plot(x, tc, label = "Costo total (QCi/2 + DS/Q)")

plt.ylabel("$")
plt.xlabel("Q")
plt.legend(loc='upper right')
plt.axis([10, 200, 0, np.max(tc)])
plt.savefig("eoq.png")
# plt.show()