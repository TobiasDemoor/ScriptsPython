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


def residuos(datos, xdat):
    y = []
    x = []
    resX = np.ones((6, 10))
    for i in range(6):
        aux = math.sqrt(xdat[i])
        resX[i] = resX[i]*aux
        for j in datos[i]:
            x.append(aux)
            y.append(j)
    m, b, r, p, err = stats.linregress(x, y)
    print(m, b, r, p, err)
    resY = np.empty((6, 10))
    for i in range(6):
        for j in range(10):
            resY[i][j] = datos[i][j] - (resX[i][j]*m+b)
    return resX, resY


def plotResiduos(datos, xdat):
    resX, resY = residuos(datos, xdat)
    for i in range(6):
        plt.plot(resX[i], resY[i], 'Db', ms=4)
        plt.ylim([-0.8, 0.8])
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
    plt.xticks(bins, np.array(
        list(map(lambda x: round(x, 3), bins))), fontsize=10)
    plt.xlabel("L^(1/2)[cm^(1/2)]")
    x = np.linspace(min(vec), max(vec), 2000)
    print(statistics.mean(vec), statistics.stdev(vec))
    y = list(map(lambda x: stats.norm.pdf(
        x, statistics.mean(vec), statistics.stdev(vec))*10, x))
    plt.plot(x, y, 'r')


def erroresRegresion(datos, xdat):
    x = []
    y = []
    for i in range(6):
        for j in datos[i]:
            x.append(math.sqrt(xdat[i]))
            y.append(j)
    m, b, r, p, err = stats.linregress(x, y)
    x = np.array(x)
    y = np.array(y)
    n = len(x)

    dy = math.sqrt(sum((y-(m*x+b))**2)/(n-2))

    sumx2 = sum(x**2)
    sumx = sum(x)**2

    Sm = dy*math.sqrt(n/(n*sumx2-sumx))
    Sb = dy*math.sqrt(sumx2/(n*sumx2 - sumx))
    return m, Sm, b, Sb


datos = [
    [5.88, 6.09, 6.09, 5.78, 5.77, 6.0, 5.97, 6.04, 5.81, 6.01],
    [7.85, 7.68, 7.46, 7.62, 7.83, 7.88, 7.54, 7.76, 8.04, 7.78],
    [9.71, 9.28, 9.54, 9.75, 9.54, 9.34, 9.30, 9.03, 9.66, 9.22],
    [10.68, 10.53, 10.41, 10.47, 10.65, 10.70, 10.75, 10.95, 10.66, 10.71],
    [11.8, 11.94, 11.45, 11.74, 11.80, 11.48, 11.34, 11.32, 11.56, 11.28],
    [12.57, 12.29, 12.62, 12.47, 12.28, 12.49, 12.56, 12.93, 12.50, 12.45],
]

xdat = [20.1, 35.1, 54.8, 70.5, 84.8, 95.1]

# scatter(datos, xdat)
# regresion(datos, xdat)
# plotResiduos(datos, xdat)
histogramaResiduos(datos, xdat)
# print(erroresRegresion(datos, xdat))

plt.show()

