import matplotlib.pyplot as plt

def prob(v):
    suma = 0
    res = []
    for i in v:
        suma += i
    for i in v:
        res.append(i/suma)
    return res

def sim1(rand, probs, vals):
    res = []
    for i in rand:
        suma = probs[0]
        j = 0
        while suma < i:
            j+=1
            suma += probs[j]
        res.append(vals[j])
    return res
#1.b

# rand = [0.2707, 0.8705, 0.7298, 0.5, 0.3901]
# b2 = [0.1353, 0.2707, 0.2707, 0.1804, 0.0902]
# b3 = [59, 166, 268, 278, 142, 87]
# suma = 0
# b3 = prob(b3)

#res = sim1(rand, b2, range(6))
# print(res)
#res = sim1(rand, b3, range(6))
# print(res)

#2
# rand = [0.0243, 0.4918, 0.5846, 0.6632, 0.8427, 0.0147, 0.8266, 0.1539, 0.0429, 0.7295]
# dat = [
#     [18, 19, 20, 21, 22, 23],
#     [15, 28, 40, 86, 75, 42],
# ]
# suma = 0
# dat[1] = prob(dat[1])
#res = sim1(rand, dat[1], dat[0])
# print(res)

#3
# pago = [0, 500, 1000, 2000, 5000, 8000, 10000]
# freq = [0.72, 0.10, 0.06, 0.05, 0.03, 0.02, 0.02]
# rand = [0.8627, 0.5938, 0.9329, 0.8281, 0.4018, 0.7837, 0.2267, 0.8649, 0.7367, 0.2143]

# res = sim1(rand, freq, pago)
# print(res.__len__() - res.count(0))
# suma = 0
# for i in res:
#     suma += i
# print(suma)

#4
prob = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]
vals = range(1,7)
rand = [0.63, 0.27, 0.15, 0.99, 0.86, 0.71, 0.74, 0.45, 0.11, 0.02, 0.15, 0.14, 0.18, 0.07, 0.14, 0.58, 0.68, 0.39, 0.31, 0.08, 0.13, 0.55, 0.47, 0.99, 0.45, 0.88, 0.54, 0.70, 0.98, 0.96]

res = sim1(rand, prob, vals)
y = []
probSim = []
for i in vals:
    count = res.count(i)
    y.append(count)
    probSim.append(count/30)

print(probSim)
plt.plot(vals, y)
plt.axis([0,7,0,10])
plt.grid()
plt.show()