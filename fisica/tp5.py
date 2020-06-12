import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import statistics
import math

muestra = [0.93, 0.96, 0.93, 0.9, 0.87, 1.03, 0.91, 0.89, 0.91, 0.94, 0.93, 0.95, 0.89, 0.95, 0.91, 0.9, 0.95, 0.85, 1, 0.9, 0.99, 0.89, 0.95, 0.88, 0.95, 0.87, 1, 0.9, 0.9, 0.91, 0.97, 0.9, 0.95, 0.86, 0.92, 0.96, 0.92, 0.94, 0.9, 0.9, 0.9, 0.91, 0.97, 0.86, 0.95, 0.93, 0.91, 0.9, 0.93, 0.91, 0.9, 0.93, 0.94, 0.91, 0.94, 0.89, 0.92, 0.86, 1, 0.93, 0.87, 0.95, 0.93, 0.93, 0.91, 0.85, 0.95, 0.96, 0.85, 0.86, 0.82, 0.91, 0.87, 0.95, 0.92, 0.95, 0.94, 0.99, 0.88, 0.89, 0.92, 0.97, 0.87, 0.97, 0.84, 0.88, 0.96, 0.95, 0.89, 0.87, 0.93, 0.91, 0.93, 0.91, 0.95, 0.87, 1, 0.97, 0.93, 0.87,
           1.09, 0.88, 0.97, 0.93, 0.97, 1, 0.85, 0.95, 0.91, 0.92, 0.87, 0.95, 0.88, 0.88, 0.8, 0.79, 0.88, 1, 0.94, 0.95, 0.98, 0.93, 0.97, 0.83, 0.97, 0.95, 0.93, 0.92, 0.82, 0.9, 0.95, 0.98, 0.92, 0.87, 0.9, 0.92, 0.95, 0.97, 0.96, 0.89, 0.92, 0.82, 0.96, 0.85, 0.97, 0.91, 0.89, 0.96, 0.94, 0.95, 0.93, 0.85, 0.92, 0.98, 0.97, 0.89, 0.92, 0.99, 0.91, 0.85, 0.97, 0.91, 0.99, 0.9, 0.87, 0.96, 0.92, 0.92, 0.86, 0.94, 0.96, 0.95, 0.96, 0.93, 0.97, 0.86, 0.97, 0.87, 1.03, 0.9, 0.87, 0.99, 0.96, 0.9, 0.9, 0.95, 0.97, 0.88, 0.97, 0.87, 0.8, 1, 0.94, 0.91, 0.94, 0.91, 0.9, 0.93, 0.95, 0.92]

mmin = min(muestra)
mmax = max(muestra)
print(statistics.mean(muestra), statistics.stdev(muestra))

def incisoA(muestra, mmin, mmax):
    k = 1 + 3.332 * math.log10(200)
    k = round(k)
    n, bins, patches = plt.hist(muestra, bins=k, edgecolor='black', linewidth=1.2)
    plt.xticks(bins, np.array(list(map(lambda x: round(x, 3), bins))), fontsize=10)
    plt.savefig('histograma1.png')
    x = np.linspace(mmin,mmax,2000)
    y = list(map(lambda x: stat.norm.pdf(x, statistics.mean(muestra), statistics.stdev(muestra))*k, x))
    plt.plot(x, y)
    plt.savefig('histograma2.png')

def incisoB(muestra):
    medias = [muestra[0]]
    errores = [0]
    for i in range(1,200):
        medias.append(statistics.mean(muestra[0:i+1]))
        errores.append(9*statistics.stdev(muestra[0:i+1])/math.sqrt(i+1))
    plt.errorbar(range(1,201), medias, yerr=errores)
    merror = max(errores)
    plt.axis([1, 200, min(medias)-merror, max(medias)+merror])
    plt.savefig("medias.png")

def incisoC(muestra):
    desviaciones = [0]
    for i in range(1,200):
        desviaciones.append(statistics.stdev(muestra[0:i+1]))
    errores = [0]
    for i in range(1,200):
        errores.append(3*statistics.stdev(desviaciones[0:i+1])/math.sqrt(2*i))
    plt.errorbar(range(1,201), desviaciones, yerr=errores)
    merror = max(errores)
    plt.axis([1, 200, min(desviaciones)-merror, max(desviaciones)+merror])
    plt.savefig("desviaciones.png")

def incisoH(muestra, mmin, mmax):
    k = 1 + 3.332 * math.log10(200)
    k = round(k)
    n, bins, patches = plt.hist(muestra, bins=k, edgecolor='black', linewidth=1.2)
    plt.xticks(bins, np.array(list(map(lambda x: round(x, 3), bins))), fontsize=10)
    media = statistics.mean(muestra)
    ymax = max(n) + 2
    plt.vlines(media, 0, ymax, 'orange', label="Media muestral", linestyles="dashed")
    plt.vlines(media+0.15, 0, ymax, 'r', label="Media ajustada", linestyles="dashed")
    plt.ylim(0, ymax)
    plt.legend(loc='upper right')
    plt.savefig("histograma3.png")

# incisoA(muestra, mmin, mmax)
# incisoB(muestra)
# incisoC(muestra)
incisoH(muestra, mmin, mmax)


plt.show()