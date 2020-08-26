# [31623, 100000)

import math

result = []

def remueve(n, v):
    d = {
            1: [1, 16, 81],
            4: [4, 49, 64],
            9: [9, 49],
            16: [1, 16, 36, 64, 81],
            25: [25],
            36: [16, 36, 64],
            49: [49, 64],
            64: [16, 36, 49, 64],
            81: [1, 16, 81]
        }
    for i in d[n]:
        try:
            v.remove(i)
        except:
            pass


for i in range(31623, 10**5):
    v = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    n = i**2
    t = n%1e2
    if t in v:
        remueve(t, v)
        t = n//1e4
        t %= 1e2
        if t in v:
            remueve(t, v)
            t = n//1e8
            t %= 1e2
            if t in v:
                s = str(n)
                j = 0
                while (j<10) and (s.count(str(j)) == 1):
                    j+=1
                if j == 10:
                    print(n)