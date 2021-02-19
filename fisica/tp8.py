import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from math import log10

diam = np.array([3.12, 4.50, 5.68, 7.1, 11.6])/1000
Ddiam = 0.03/1000
a = [
    [0.0124, 0.013, 0.013, 0.012],
    [0.029, 0.030, 0.029, 0.030],
    [0.054, 0.053, 0.054, 0.053],
    [0.112, 0.111, 0.110, 0.109],
    [0.33, 0.33, 0.33, 0.33]
]
Da = [
    [3 * 0.0002, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

x, y = [], []
xerr, yerr = [], []
g = 9.80665
for i, d in enumerate(diam):
    x.extend([d]*len(a[i]))
    xerr.extend([Ddiam]*len(a[i]))
    y.extend([j/g for j in a[i]])
    yerr.extend([j/g for j in Da[i]])


def analisis():
    global x, y

    logx = [log10(i) for i in x]
    logy = [log10(i) for i in y]
    m, b, r, p, err = stats.linregress(logx, logy)
    plt.plot(x, [10**(m*i + b) for i in logx],
             '-r', label="Recta Aproximación")
    # plt.plot(x, [10**b*i**(5/2) for i in x], '-b', label="Recta Teórica")
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel(r"$Q \ [\frac {kg} {s}]$")
    plt.xlabel(r"$D \ [m]$")
    print(r, m, 10**b)


def analisisCompensado():
    global x, y, yerr

    y = [i**(2/5) for i in y]
    for i, yi in enumerate(y):
        yerr[i] *= 2/5 * yi**(-3/5)
    m, b, r, p, err = stats.linregress(x, y)
    plt.plot(x, [m*i + b for i in x], '-r', label="Recta Aproximación")
    plt.ylabel(r'$Q^{\frac {2} {5}} \  [\frac {kg} {s} ^ {\frac {2} {5}}]$')
    plt.xlabel(r"$D \ [m]$")
    print(r, m, b, b/m)


analisis()
# analisisCompensado()

plt.errorbar(x, y, fmt='.k', xerr=xerr, yerr=yerr,
             label="Experimental", capsize=2)
plt.legend()
plt.grid(True, which='both')
plt.show()
