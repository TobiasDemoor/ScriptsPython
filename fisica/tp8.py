import matplotlib.pyplot as plt
import scipy.stats as stats
from math import log10

diam = [3.12, 4.50, 5.68, 7.1, 11.6]
Ddiam = [0.03, 0.03, 0.03, 0.03, 0.02]
a = [
    [0.0124, 0.013, 0.013, 0.012],
    [0.029, 0.030, 0.029, 0.030],
    [0.054, 0.053, 0.054, 0.053],
    [0.112, 0.111, 0.110, 0.109],
    [0.33, 0.33, 0.33, 0.33]
]

x = []
y = []
g = 9.80665
for i, d in enumerate(diam):
    x.extend([d]*len(a[i]))
    y.extend([j/g for j in a[i]])

def analisis():
    global x, y

    logx = [log10(i) for i in x]
    logy = [log10(i) for i in y]
    m, b, r, p, err = stats.linregress(logx, logy)
    plt.plot(x, [10**(m*i + b) for i in logx])
    plt.xscale('log')
    plt.yscale('log')
    print(r, m)

def analisisCompensado():
    global x, y

    y = [i**(2/5) for i in y]
    m, b, r, p, err = stats.linregress(x, y)
    plt.plot(x, [m*i + b for i in x])
    print(r, m)



analisis()
# analisisCompensado()

plt.plot(x, y, '.k')
plt.grid(True, which='both')
plt.show()

