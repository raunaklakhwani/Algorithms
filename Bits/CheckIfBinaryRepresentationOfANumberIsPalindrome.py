from math import log, floor
i = 21
l = 0
h = int(floor(log(i, 2)))
print bin(i)
# print h
while l <= h:
    m = i & (1 << l | 1 << h)
    # print m,(m >> l),(m >> h)
    if ((m >> l) & 1) == ((m >> h) & 1):
        l = l + 1
        h = h - 1
    else:
        print False
        break
else:
    print True
        
