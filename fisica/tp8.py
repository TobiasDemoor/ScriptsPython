from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from math import log10, exp, sqrt

def errorLog(datos, error):
    le = log10(exp(1))
    res = []
    for i, d in enumerate(error):
        res.append(le*d/datos[i])
    return res

def erroresRegresion(paramx, paramy):
    m, b, r, p, err = stats.linregress(paramx, paramy)
    x = np.array(paramx)
    y = np.array(paramy)
    n = len(x)

    dy = sqrt(sum((y-(m*x+b))**2)/(n-2))

    sumx2 = sum(x**2)
    sumx = sum(x)**2

    Sm = dy*sqrt(n/(n*sumx2-sumx))
    Sb = dy*sqrt(sumx2/(n*sumx2 - sumx))
    return m, Sm, b, Sb

diam = np.array([3.12, 4.50, 5.68, 7.1, 11.6])/1000
Ddiam = 0.03/1000

a = [
    [0.0124, 0.013, 0.013, 0.012],
    [0.029, 0.030, 0.029, 0.030],
    [0.054, 0.053, 0.054, 0.053],
    [0.112, 0.111, 0.110, 0.109],
    [0.33, 0.33, 0.33, 0.33]
]

x, y = [], []
xerr = []
g = 9.80665
for i, d in enumerate(diam):
    x.extend([d]*len(a[i]))
    xerr.extend([Ddiam]*len(a[i]))
    y.extend([j/g for j in a[i]])


# le = log10(exp(1))
# for d in diam:
#     error = le*Ddiam/d
#     print(f"{error} ({(100*error/log10(d))}%)")

def analisis():
    global x, y

    logx = [log10(i) for i in x]
    logy = [log10(i) for i in y]
    m, b, r, p, err = stats.linregress(logx, logy)
    plt.plot(x, [10**(m*i + b) for i in logx],
             '-r', label="Recta Aproximación")

    # m2,b2,r,p,err2 = stats.linregress(logy, logx)
    # plt.plot([10**(m2*i + b2) for i in logy], y,
    #          '-b', label="Recta Aproximación x = f(y)")
    # print(f"m: {m} ; {1/m2}") # comparo pendiente de y = f(x) y x = g(y)
    # print(f"b: {b} ; {-b2/m2}") # comparo ordenada de y = f(x) y x = g(y)
    # print(f"err: {err} ; {err2/m2**2}") # comparo error de y = f(x) y x = g(y)

    # plt.plot(x, [10**b*i**(5/2) for i in x], '-b', label="Recta Teórica")
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel(r"$Q \ [\frac {kg} {s}]$")
    plt.xlabel(r"$D \ [m]$")
    print(erroresRegresion(logx,logy))
    print(r, m, b, err)


def analisisCompensado():
    global x, y, yerr

    y = [i**(2/5) for i in y]
    m, b, r, p, err = stats.linregress(x, y)
    plt.plot(x, [m*i + b for i in x], '-r', label="Recta Aproximación")
    plt.ylabel(r'$Q^{\frac {2} {5}} \  [\frac {kg} {s} ^ {\frac {2} {5}}]$')
    plt.xlabel(r"$D \ [m]$")
    print(erroresRegresion(x,y))
    print(r, m, b, err, b/m)


analisis()
# analisisCompensado()

plt.errorbar(x, y, fmt='.k', xerr=xerr, label="Experimental", capsize=2)
plt.legend()
plt.grid(True, which='both')
plt.show()
