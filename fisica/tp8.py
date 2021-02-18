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
for i, d in enumerate(diam):
    x.extend([log10(d)]*len(a[i]))
    y.extend(a[i])
    # x.extend([d]*len(a[i]))
    # y.extend([j**(2/5) for j in a[i]])

m, b, r, p, err = stats.linregress(x, y)

print(r)

plt.plot(x,y, '.')
plt.plot(x, [m*i + b for i in x])
plt.show()

