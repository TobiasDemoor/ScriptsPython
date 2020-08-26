def naturales(n):
    yield n
    yield from naturales(n+1)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n!=0)

nat = naturales(2)
s = sieve(nat)
for i in range(10):
    print(next(s))