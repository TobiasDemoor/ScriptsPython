def lq(m, l):
    return (l**2)/(m*(m-l))

def lt(m,l):
    return lq(m,l) + l/m

def wq(m,l):
    return lq(m,l)/l

def wt(m,l):
    return wq(m,l) + 1/m

def pw(m,l):
    return l/m

def pn(m,l,n):
    aux =pw(m,l)
    return (aux**n)*(1-aux)
