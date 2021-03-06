import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
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


class Dist:
    def __init__(self, valores):
        self.valores = valores

    def setValores(self, valores):
        self.valores = valores

    def getValores(self):
        return self.valores

    def inversa(self, prob):
        raise NotImplementedError()

    def simulacion(self, rand):
        res = []
        for i in rand:
            res.append(self.inversa(i))
        return res

    def distSimulacion(self, rand):
        sim = self.simulacion(rand)
        freq = []
        for i in self.valores:
            freq.append(sim.count(i))
        return DistSimulada(self.valores, freq, sim)


class DistExp(Dist):
    def __init__(self, valores, probAcum):
        self.probAcum = probAcum
        super().__init__(valores)

    def setProbAcum(self, probAcum):
        self.probAcum = probAcum

    def getProbAcum(self):
        return self.probAcum

    def inversa(self, prob):
        i = 0
        while not(self.probAcum[i] >= prob):
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


class DistSimulada(DistExp):
    def __init__(self, valores, frecuencias, muestra):
        self.muestra = muestra
        suma = sum(frecuencias)
        aux = 0
        prob = []
        for i in frecuencias:
            aux += i/suma
            prob.append(aux)
        super().__init__(valores, prob)

    def getMuestra(self):
        return self.muestra


class DistTeoricaDiscreta(Dist):
    epsilon = 1e-4

    def __init__(self, funcion, techo=0, piso=0):
        self.funcion = funcion
        self.piso = piso
        if techo == 0:
            i = 0
            while funcion(i) > DistTeoricaDiscreta.epsilon:
                i += 1
            techo = i
        self.techo = techo
        super().__init__(range(piso, techo+1))

    def setPiso(self, piso):
        self.piso = piso
        super().setValores(range(piso, self.techo+1))

    def setTecho(self, techo):
        self.techo = techo
        super().setValores(range(self.piso, techo+1))

    def getProbAcum(self):
        prob = []
        aux = 0
        for i in self.valores:
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

    def prob(self, x):
        return self.funcion(x)


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
    m, b, r, _ = stats.linregress(x, y)
    plt.plot(x, y, 'o')
    ajust = []
    for i in x:
        ajust.append(b + m*i)
    plt.plot(x, ajust, 'r')
    return m, b, r
