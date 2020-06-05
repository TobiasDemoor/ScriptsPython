import matplotlib.pyplot as plt
import numpy as num
import math
import scipy.stats as stat
import statistics
import random


def prob(v):
    suma = sum(v)
    res = []
    for i in v:
        res.append(i/suma)
    return res


def sim1(rand, probs, vals):
    res = []
    for i in rand:
        suma = probs[0]
        j = 0
        while suma < i:
            j += 1
            suma += probs[j]
        res.append(vals[j])
    return res


def poisson(mu, k):
    return (num.e**(-mu) * mu**k)/math.factorial(k)


def desvStd(v, mu=None):
    sigma = 0
    if mu == None:
        mu = sum(v)/v.__len__()
    for i in v:
        sigma += (i - mu)**2
    sigma /= v.__len__()
    return math.sqrt(sigma)


def regr(x, y):
    m, b, r, p, err = stat.linregress(x, y)
    plt.plot(x, y, 'o')
    ajust = []
    for i in prob:
        ajust.append(b + m*i)
    plt.plot(x, ajust, 'r')
    return m, b, r

# 1.b
# rand = [0.2707, 0.8705, 0.7298, 0.5, 0.3901]
# b2 = [0.1353, 0.2707, 0.2707, 0.1804, 0.0902]
# b3 = [59, 166, 268, 278, 142, 87]
# suma = 0
# b3 = prob(b3)

# res = sim1(rand, b2, range(6))
# print(res)
# res = sim1(rand, b3, range(6))
# print(res)

# 2
# rand = [0.0243, 0.4918, 0.5846, 0.6632, 0.8427,
#         0.0147, 0.8266, 0.1539, 0.0429, 0.7295]
# dat = [
#     [18, 19, 20, 21, 22, 23],
#     [15, 28, 40, 86, 75, 42],
# ]
# suma = 0
# dat[1] = prob(dat[1])
# res = sim1(rand, dat[1], dat[0])
# print(res)

# 3
# pago = [0, 500, 1000, 2000, 5000, 8000, 10000]
# freq = [0.72, 0.10, 0.06, 0.05, 0.03, 0.02, 0.02]
# rand = [0.8627, 0.5938, 0.9329, 0.8281, 0.4018,
#         0.7837, 0.2267, 0.8649, 0.7367, 0.2143]

# res = sim1(rand, freq, pago)
# print(res.__len__() - res.count(0))
# suma = sum(res)
# print(suma)


# 4
# prob = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]
# vals = range(1, 7)
# rand = [0.63, 0.27, 0.15, 0.99, 0.86, 0.71, 0.74, 0.45, 0.11, 0.02, 0.15, 0.14, 0.18, 0.07,
#         0.14, 0.58, 0.68, 0.39, 0.31, 0.08, 0.13, 0.55, 0.47, 0.99, 0.45, 0.88, 0.54, 0.70, 0.98, 0.96]

# res = sim1(rand, prob, vals)
# y = []
# probSim = []
# aux = 0
# for i in vals:
#     count = res.count(i)
#     y.append(count)
#     aux += count/30
#     probSim.append(aux)

# aux = 0
# for k in range(6):
#     aux += prob[k]
#     prob[k] = aux

# m, b, r = regr(prob, probSim)

# print(r**2)
# print(probSim)
# # plt.plot(vals, y)
# # plt.axis([0, 7, 0, 10])
# plt.grid()
# plt.show()


# 5
# rand = [0.6327, 0.9543, 0.1599, 0.6791, 0.8671, 0.1508, 0.7445, 0.3030, 0.1102, 0.1041, 0.1514, 0.2003, 0.1807, 0.0637, 0.1458,
#         0.5408, 0.6839, 0.4592, 0.3108, 0.8364, 0.1355, 0.5595, 0.4799, 0.7572, 0.4588, 0.4383, 0.5470, 0.8650, 0.9896, 0.9911]
# media = 5
# prob = []
# for k in range(17):
#     prob.append(poisson(media, k))

# res = sim1(rand, prob, range(17))

# suma = sum(res)
# mu = suma/rand.__len__()

# sigma = statistics.stdev(res)

# probSim = []
# aux = 0
# for k in range(17):
#     aux += res.count(k)/30
#     probSim.append(aux)
# aux = 0
# for k in range(17):
#     aux += prob[k]
#     prob[k] = aux

# m, b, r = regr(prob, probSim)

# print(suma)
# print(mu)
# print(sigma)
# print(r**2)
# plt.show()


# 6
dReap = [2, 3, 4, 5, 6, 7, 8]
pReap = [5, 13, 17, 27, 23, 10, 5]
dCons = [70, 80, 90, 100, 110, 120, 130]
pCons = [7, 10, 18, 28, 21, 10, 6]

aux = sum(pReap)
pReap[:] = [x/aux for x in pReap]
aux = sum(pCons)
pCons[:] = [x/aux for x in pCons]

r1 = []
r2 = []

for i in range(30):
    r1.append(random.random())
    r2.append(random.random())

simReap = sim1(r1, pReap, dReap)
simCons = sim1(r1, pCons, dCons)
simR = list(map(lambda d, L: d*L, simCons, simReap))

espera = -1
stock = 200
gastos = 0

# ss = statistics.stdev(simReap)*stat.norm.ppf(0.90)
ss = 0
for i in range(30):
    stock -= simCons[i]
    if stock > 0:
        gastos += stock*0.3
    if espera > 0:
        espera -= 1
    elif espera == 0:
        espera = -1
        gastos += -1*stock*2
        stock += 500
    elif stock < simCons[i]*simReap[i] + ss:
        espera = simReap[i]
        print("Pedido solicitado dia %d", i)

print(gastos)
# print(simReap)
# print(simCons)
# print(sum(simR)/30)
