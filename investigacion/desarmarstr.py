s = input("Dale bo: ")
l = s.split(' ')
t = l[0].split(':')
t[0] = int(t[0])
t[1] = int(t[1])
if t[0] == 12:
    t[0] = 0
t[0] = t[0] + (12 if l[1]=="PM" else 0)
print("%02d:%02d"% (t[0], t[1]))
