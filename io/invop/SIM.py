import matplotlib.pyplot as plt
import scipy.stats as stats
import math

class DistExpFactory:
    @staticmethod
    def fromProbAbs(valores, probAbs):
        s = 0
        probAcum = []
        for i in probAbs:
            s += i
            probAcum.append(s)
        return DistExp(valores, probAcum)

    @staticmethod
    def fromFrecuencia(valores, frecuencias):
        suma = sum(frecuencias)
        prob = []
        for i in frecuencias:
            prob.append(i/suma)
        return DistExpFactory.fromProbAbs(valores, prob)

    @staticmethod
    def fromMuestra(muestra):
        valores = list(set(muestra))
        valores.sort()
        cant = len(muestra)
        probAcum = []
        aux = 0
        for i in valores:
            aux += muestra.count(i)/cant
            probAcum.append(aux)
        return DistExp(valores, probAcum)


class DistExp:
    def __init__(self, valores, probAcum):
        self.valores = valores
        self.probAcum = probAcum

    def setProbAcum(self, probAcum):
        self.probAcum = probAcum

    def getProbAcum(self):
        return self.probAcum

    def setValores(self, valores):
        self.valores = valores

    def getValores(self):
        return self.valores

    def inversa(self, prob):
        i = 0
        while not(self.probAcum[i] > prob):
            i += 1
        return self.valores[i]

    def prob(self, x):
        res = 0
        i = 0
        while x > self.valores[i]:
            i += 1
        if self.valores[i] == x:
            if i > 0:
                res = (self.probAcum[i]-self.probAcum[i-1])
            else:
                res = self.probAcum[i]
        return res


class DistTeoricaEntera:
    def __init__(self, funcion):
        self.funcion = funcion

    def getProbAcum(self, tope):
        prob = []
        aux = 0
        for i in range(tope):
            aux += self.funcion(i)
            prob.append(aux)
        return prob

    def inversa(self, prob):
        i = 0
        acum = self.funcion(i)
        while not(acum > prob):
            i += 1
            acum += self.funcion(i)
        return i


def simulacion(rand, inversa):
    res = []
    for i in rand:
        res.append(inversa(i))
    return res


def poisson(mu, k):
    return (np.e**(-mu) * mu**k)/math.factorial(k)


def exponInv(lam, prob):
    return stats.expon.ppf(prob, 0, lam)


def normInv(mu, sigma, prob):
    return stats.norm.ppf(prob)*sigma+mu


def regr(x, y):
    m, b, r, p, err = stats.linregress(x, y)
    plt.plot(x, y, 'o')
    ajust = []
    for i in x:
        ajust.append(b + m*i)
    plt.plot(x, ajust, 'r')
    return m, b, r