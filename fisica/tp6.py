import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import statistics
import math


def scatter(datos, xdat):
    x = []
    y = []
    for i in range(6):
        for j in datos[i]:
            x.append(xdat[i])
            y.append(j)
    plt.plot(x, y, 'xb', ms=4)
    plt.xlabel("L[cm]")
    plt.ylabel("T[s]")
    plt.grid()



def regresion(datos, xdat):
    x = []
    y = []
    for i in range(6):
        for j in datos[i]:
            x.append(math.sqrt(xdat[i]))
            y.append(j)
    m, b, r, p, err = stats.linregress(x, y)
    print(r**2)
    ajusty = []
    ajustx = []
    for i in xdat:
        aux = math.sqrt(i)
        ajustx.append(aux)
        ajusty.append(b + m*aux)
    plt.plot(x, y, 'xb')
    plt.plot(ajustx, ajusty, 'r')
    plt.xlabel("L^(1/2)[cm^(1/2)]")
    plt.ylabel("T[s]")
    plt.grid()

def residuos (datos, xdat):
    x = []
    y = []
    resX = []
    for i in range(6):
        auxV = []
        for j in datos[i]:
            aux = math.sqrt(xdat[i])
            auxV.append(aux)
            x.append(aux)
            y.append(j)
        resX.append(auxV)
    m, b, r, p, err = stats.linregress(x, y)
    resY = []
    for i in range(6):
        auxV = []
        for j in range(10):
            auxV.append(datos[i][j] - (resX[i][j]*m+b))
        resY.append(auxV)
    return resX, resY

    

def plotResiduos(datos, xdat):
    resX, resY = residuos(datos, xdat)
    for i in range(6):
        plt.plot(resX[i], resY[i], 'Db', ms =4)
        plt.ylim([0.8, -0.8])
    plt.xlabel("L^(1/2)[cm^(1/2)]")
    plt.ylabel("T[s]")
    plt.grid()

def histogramaResiduos(datos, xdat):
    resX, resY = residuos(datos, xdat)
    vec = []
    for i in resY:
        vec.extend(i)
    k = 1 + 3.332 * math.log10(len(vec))
    k = round(k)
    n, bins, patches = plt.hist(vec, bins=k, edgecolor='black', linewidth=1.2)
    plt.xticks(bins, np.array(list(map(lambda x: round(x, 3), bins))), fontsize=10)
    plt.xlabel("L^(1/2)[cm^(1/2)]")
    x = np.linspace(min(vec),max(vec),2000)
    print(statistics.mean(vec), statistics.stdev(vec))
    y = list(map(lambda x: stats.norm.pdf(x, statistics.mean(vec), statistics.stdev(vec))*k, x))
    plt.plot(x, y)



datos = [
    [5.88, 6.09, 6.09, 5.78, 5.77, 6.0, 5.97, 6.04, 5.81, 6.01],
    [7.85, 7.68, 7.46, 7.62, 7.83, 7.88, 7.54, 7.76, 8.04, 7.78],
    [9.71, 9.28, 9.54, 9.75, 9.54, 9.34, 9.30, 9.03, 9.66, 9.22],
    [10.24, 10.22, 10.33, 10.38, 10.06, 10.59, 10.14, 10.47, 10.61, 10.54],
    [11.8, 11.94, 11.45, 11.74, 11.8, 11.18, 11.34, 11.32, 11.56, 11.28],
    [12.57, 12.29, 12.47, 12.28, 12.49, 12.56, 12.93, 12.50, 12.45, 12.62],
]

xdat = [20, 35, 54.8, 70.5, 84.7, 95.1]

histogramaResiduos(datos, xdat)
plt.show()
# nd = statistics.NormalDist(37, math.sqrt(sum(varianzas)))
# # print("Prob(x < 20) = ", nd.cdf(32))
# print(nd.inv_cdf(0.8), " < p < ",nd.inv_cdf(0.9))
