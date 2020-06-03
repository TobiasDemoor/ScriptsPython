# def lq(m, l):
#     return (l**2)/(m*(m-l))

# def lt(m,l):
#     return lq(m,l) + l/m

# def wq(m,l):
#     return lq(m,l)/l

# def wt(m,l):
#     return wq(m,l) + 1/m

# def pw(m,l):
#     return l/m

# def pn(m,l,n):
#     aux =pw(m,l)
#     return (aux**n)*(1-aux)

# print(lq(1/20, 1/30))
# print(lt(1/20, 1/30))
# print(wq(1/20, 1/30))
# print(wt(1/20, 1/30))
# print(pw(1/20, 1/30))
# print(pn(1/20, 1/30, 0))
# print(1-(pn(1/20, 1/30, 3) + pn(1/20, 1/30, 2) + pn(1/20, 1/30, 1) + pn(1/20, 1/30, 0)))
vec = [5.4545, 2.041, 1.740, 1.6818]
for i in range(4):
    print(vec[i]*400+250*(i+2))