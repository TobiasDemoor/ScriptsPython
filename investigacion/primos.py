def naturales(n):
    yield n
    yield from naturales(n+1)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n!=0)

nat = naturales(2)
s = sieve(nat)
for i in range(100):
    print(next(s))

def cords(n):
    maxP = [1,1]
    pos = [0,0]
    indice = 0
    inc = 1
    for i in range(1,n+1):
        print(pos)
        if pos[indice] == maxP[indice]:
            indice += 1
            indice %= 2
            if pos == maxP:
                maxP[indice] *= -1
                inc = -1
        pos[indice] += inc