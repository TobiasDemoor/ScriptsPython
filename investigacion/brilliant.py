va = 0
ma = 13
vp = 12
mp = 1
for i in range(9):
    va = (ma*va-mp*(va-vp))/(ma-mp)
    ma -= mp
    print(va, ma)
