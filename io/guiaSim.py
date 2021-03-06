import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import random
import numpy as np
import math
import statistics
from invop.SIM import *

# region 1.b
# rand = [0.2707, 0.8705, 0.7298, 0.5, 0.3901]

# distexp = DistExpFactory.fromProbAbs(
#     range(6),
#     [0.1353, 0.2707, 0.2707, 0.1804, 0.0902]
# )
# print(pd.DataFrame({"rnd":rand, "sim": distexp.simulacion(rand)}))

# distexp = DistExpFactory.fromFrecuencia(
#     range(6),
#     [59, 166, 268, 278, 142, 87]
# )
# print(pd.DataFrame({"rnd":rand, "sim": distexp.simulacion(rand)}))
# endregion

# region 2
# rand = [0.0243, 0.4918, 0.5846, 0.6632, 0.8427,
#         0.0147, 0.8266, 0.1539, 0.0429, 0.7295]

# distexp = DistExpFactory.fromFrecuencia(
#     [18, 19, 20, 21, 22, 23],
#     [15, 28, 40, 86, 75, 42]
# )

# print(pd.DataFrame({"rnd":rand, "sim": distexp.simulacion(rand)}))
# endregion

# region 3
# rand = [0.8627, 0.5938, 0.9329, 0.8281, 0.4018,
#         0.7837, 0.2267, 0.8649, 0.7367, 0.2143]

# distexp = DistExpFactory.fromProbAbs(
#     [0, 500, 1000, 2000, 5000, 8000, 10000],
#     [0.72, 0.10, 0.06, 0.05, 0.03, 0.02, 0.02]
# )

# res = distexp.simulacion(rand)
# print(len(res) - res.count(0))
# suma = sum(res)
# print(suma)
# endregion

# region 4
# rand = [0.63, 0.27, 0.15, 0.99, 0.86, 0.71, 0.74, 0.45, 0.11, 0.02, 0.15, 0.14, 0.18, 0.07,
#         0.14, 0.58, 0.68, 0.39, 0.31, 0.08, 0.13, 0.55, 0.47, 0.99, 0.45, 0.88, 0.54, 0.70, 0.98, 0.96]
# dias = {1: "lunes", 2:"martes", 3:"miercoles", 4:"jueves", 5:"viernes", 6:"sabado"}

# distexp = DistExpFactory.fromProbAbs(range(1, 7), [0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
# distsim = distexp.distSimulacion(rand)

# df = pd.DataFrame({"rand": rand, "dias":distsim.getMuestra()})
# df = df.transpose()
# print(df)

# plan = np.zeros((6,4))
# for i in distsim.getMuestra():
#     j = list(plan[i-1]).index(min(plan[i-1]))
#     plan[i-1][j] += 1

# plan = pd.DataFrame(plan).transpose()
# plan.columns = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
# print(plan)

# # m, b, r = regr(distexp.getProbAcum(), distsim.getProbAcum())
# # print(r**2)
# # print(distsim.getProbAcum())
# # plt.grid()

# data = np.array(distsim.getMuestra())
# d = np.diff(np.unique(data)).min()
# left_of_first_bin = data.min() - float(d)/2
# right_of_last_bin = data.max() + float(d)/2
# plt.hist(data, np.arange(left_of_first_bin, right_of_last_bin + d, d))

# plt.show()
# endregion

# region 5
# rand = [0.6327, 0.9543, 0.1599, 0.6791, 0.8671, 0.1508, 0.7445, 0.3030, 0.1102, 0.1041, 0.1514, 0.2003, 0.1807, 0.0637, 0.1458,
#         0.5408, 0.6839, 0.4592, 0.3108, 0.8364, 0.1355, 0.5595, 0.4799, 0.7572, 0.4588, 0.4383, 0.5470, 0.8650, 0.9896, 0.9911]
# media = 5

# dist = DistTeoricaDiscreta(lambda x: poisson(media, x))

# res = simulacion(rand, dist.inversa)
# suma = sum(res)
# mu = suma/len(rand)

# sigma = statistics.stdev(res)
# distsim = dist.distSimulacion(rand)

# m, b, r = regr(dist.getProbAcum(), distsim.getProbAcum())

# print(suma)
# print(mu)
# print(sigma)
# print(r**2)
# plt.show()
# endregion

# region 6
# dReap = [2, 3, 4, 5, 6, 7, 8]
# fReap = [5, 13, 17, 27, 23, 10, 5]
# dCons = [70, 80, 90, 100, 110, 120, 130]
# fCons = np.array([7, 10, 18, 28, 21, 10, 6])

# distExpL = DistExpFactory.fromFrecuencia(dReap, fReap)
# distExpD = DistExpFactory.fromFrecuencia(dCons, fCons)


# r1 = [0.91, 0.59, 0.88, 0.19, 0.75, 0.45, 0.43, 0.27, 0.15, 0.25, 0.06, 0.45, 0.22, 0.14, 0.80,
#     0.08, 0.62, 0.52, 0.68, 0.89, 0.39, 0.70, 0.64, 0.51, 0.25, 0.55, 0.84, 0.35, 0.28, 0.81]
# r2 = [0.63, 0.27, 0.15, 0.99, 0.86, 0.71, 0.74, 0.45, 0.11, 0.02, 0.15, 0.14, 0.18, 0.07, 0.14,
#     0.58, 0.68, 0.39, 0.31, 0.08, 0.13, 0.55, 0.47, 0.99, 0.45, 0.88, 0.54, 0.70, 0.98, 0.96]


# simReap = distExpL.simulacion(r1)
# simCons = distExpD.simulacion(r2)


# arribo = -1
# stock = 500
# gastos = 0

# df = pd.DataFrame({"stock":[], "consumo":[], "R": [], "cAlm":[], "cFalta":[], "tReap": []})
# ss = statistics.stdev(dCons)*math.sqrt(statistics.mean(dReap))*stats.norm.ppf(0.90);
# almacenado = 0
# faltante = 0
# # ss = 0
# R = statistics.mean(dCons)*statistics.mean(dReap) + ss
# d= statistics.mean(dCons)
# j = 0
# for i in range(30):
#     if i == arribo:
#         if stock < 0:
#             faltante -= stock
#             stock = 0
#         stock += 500
#     stock -= simCons[i]
#     if stock > 0:
#         almacenado += stock
#     if (i >= arribo) and (stock <= d*simReap[j] + ss):
#         arribo = i + simReap[j]
#         j+= 1
#         print(f"Pedido solicitado dia {i}")
#     df.loc[i] = [stock, simCons[i], d*simReap[j] + ss, almacenado, faltante, simReap[j]]

# print(df)
        
# print(f"Gastos totales: $ {almacenado*0.3+faltante*2}")
# endregion

# region 7
# rand = [0.5029, 0.7333, 0.7818, 0.4541, 0.0727, 0.2290, 0.3246,
#         0.8961, 0.8025, 0.5754, 0.4769, 0.9083, 0.0278, 0.8062, 0.1894]
# util = 120
# gasto = 150
# ganancia = 0
# for i in rand:
#     ganancia += 50*util
#     extra = int(normInv(50, 2, i))-50
#     if extra > 0:
#         ganancia -= extra*gasto
#     else:
#         ganancia += extra*util
# print(ganancia/len(rand))
# endregion

# region 8
# hist = []
# n = 6
# for j in range(30):
#     esperando = 0
#     espera = 120/n
#     for i in range(1, n):
#         espera += normInv(4, 1, random.random())
#         entrePersonas = exponInv(2, random.random())
#         espera -= entrePersonas
#         while espera > 0:
#             esperando += 1
#             entrePersonas = exponInv(2, random.random())
#             espera -= entrePersonas
#         hist.append(esperando)
#         esperando = 1
#         espera += 120/n

# print(sum(hist)/(30*n))
# endregion

# region parcial 2008
n = 1000
mu = 1/24
lam = 1/21
lim = 9
crechazo = 20
calquiler = 10
calquiler = 0
rechazados = 0
tfinal = []
colas = []

for i in range(n):
    cola = 0
    t1 = t0 = exponInv(lam, random.random())
    while t0 < 1:
        t1 += exponInv(lam, random.random())
        tf = t0 + exponInv(mu, random.random())
        while (tf > t1) and (t1< 1):
            if cola == lim:
                rechazados += 1
            else:
                cola += 1
            t1 += exponInv(lam, random.random())
        colas.append(cola)
        if cola > 0:
            cola -= 1
            t0 = tf
        else:
            t0 = t1
    tfinal.append(t0)

print(rechazados*crechazo/n + calquiler)
print(statistics.mean(tfinal), statistics.stdev(tfinal))
data = np.array(colas)
d = np.diff(np.unique(data)).min()
left_of_first_bin = data.min() - float(d)/2
right_of_last_bin = data.max() + float(d)/2
plt.hist(data, np.arange(left_of_first_bin, right_of_last_bin + d, d))
plt.show()
# endregion