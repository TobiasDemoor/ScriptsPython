import matplotlib.pyplot as plt
from math import log
import scipy.stats as stats

q = [700, 1500, 2500, 10000, 25000]
p = [115000, 250000, 350000, 950000, 1400000]

x = [log(i) for i in q]
y = [log(i) for i in p]

plt.plot(x, y, '.')
m, b, r, p, err = stats.linregress(x, y)
plt.plot(x, [m*i+b for i in x])
plt.show()
print(m, b, r, p, err)