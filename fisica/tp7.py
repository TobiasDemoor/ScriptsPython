import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from math import log10, exp, cos, pi

def errorLog(datos, error):
    le = log10(exp(1))
    res = []
    for i, d in enumerate(error):
        res.append(le*d/datos[i])
    return res

# valores de la primer experiencia
l = [0.190, 0.200, 0.212, 0.227, 0.245, 0.269, 0.300, 0.347, 0.425, 0.600]
Dl = 0.007
R1 = [540, 590, 700, 838, 1077, 1485, 2050, 2460, 4030, 8470]
DR1 = [6, 7, 8, 9, 11, 14, 36, 40, 52, 88]
I = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
DI = []
for i in range(len(I)):
    DI.append(I[i]*2*Dl*(1/l[i] + 1/l[0]))


logR1 = [log10(i) for i in R1]
DlogR1 = errorLog(R1, DR1)

logI = [log10(i) for i in I]
DlogI = errorLog(I, DI)

m, b, r, p, err = stats.linregress(logR1, logI)
print(r, m, b)

plt.errorbar(R1, I, fmt='.k', yerr=DI, xerr=DR1, capsize=2, label="Experimental")
plt.plot(R1, [10**(m*i + b) for i in logR1], '-r', label="Recta aproximación")

# for i, d in enumerate(DlogI):
#     try:
#         print(f"{d} ({(100*d/logI[i])}%)")
#     except:
#         pass

# for i, d in enumerate(DlogR1):
#     print(f"{d} ({(100*d/logR1[i])}%)")

plt.yscale('log')
plt.xscale('log')
plt.ylabel('I[UP]')
plt.xlabel('R[Ω]')
plt.xlim([10**2, 10**4])

# valores de la segunda experiencia
theeta = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180,
          200, 220, 240, 260, 280, 300, 320, 340, 360]
Dtheeta = 5
R2 = [1770, 1980, 3110, 7650, 160000, 26400, 5880, 2510, 1925,
      1820, 2170, 3420, 9300, 115000, 36000, 5270, 2760, 2020, 1830]
DR2 = [16, 18, 45, 81, 1480, 411, 67, 40, 17,
       17, 37, 47, 94, 1120, 488, 62, 42, 36, 17]

I2 = []
DI2 = []
for i in range(len(R2)):
    imin = 10**(m*log10(R2[i] + DR2[i]) + b)
    imax = 10**(m*log10(R2[i] - DR2[i]) + b)
    I2.append((imax + imin)/2)
    DI2.append((imax - imin)/2)

# plt.plot(theeta, I2, '-r', label="Experimental")
# plt.errorbar(theeta, I2, fmt='.k', xerr=Dtheeta, yerr=DI2, capsize=3, label="Experimental")

# plt.xticks(np.linspace(0, 360, 10))
# plt.ylabel('I[UP]')
# plt.xlabel('θ[°]')

# analisis ley de malus
theeta2 = np.linspace(0, 360, 80)
I3 = [I2[0]*cos(i*pi/180)**2 for i in theeta2]
# plt.plot(theeta2, I3, label="Malus")

plt.legend()
plt.grid(True, which='both')
plt.show()
