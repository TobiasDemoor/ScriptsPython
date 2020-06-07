import sys

def ackermann(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    else: # m>0 and n>0
        return ackermann(m-1, ackermann(m,n-1))

print(ackermann(4,0))
# sys.setrecursionlimit(10000)
# print(ackermann(4,1))