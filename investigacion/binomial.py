import sys


def gof(n,a):
    if n == 1:
        return a
    else:
        return gof(n-1, a*n)

def fact(n):
    return gof(n, 1)

def comb(n, p):
    return fact(n)/(fact(p)*fact(n-p))

def p(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

# sys.setrecursionlimit(10000)
# acum = 0
# for i in range(1, 8001):
#     acum += p(1, i, 1/8000)

print((7999/8000)**8000)