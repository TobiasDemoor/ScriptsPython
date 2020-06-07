import sys

def gof(n,a):
    if n == 1:
        return a
    else:
        return gof(n-1, a*n)

def fact(n):
    return gof(n, 1)

# tail recursion
def go(n, a, b):
    if n == 0 :
        return a
    elif n == 1:
        return b
    else:
        return go(n-1, b, a+b)

def fib(n):
    return go(n,0,1)

# funcion recursiva caca
def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

sys.setrecursionlimit(10000)
n = fact(69)
print(n)
i = 0
while n>0:
    n //= 2
    i += 1
print(i)
# fact(5000)
# print(fib(5000))

