N = 20

a = 1
b = 1
print a
print b
for i in xrange(3,N):
    print len(str(a+b)),b,a + b
    a,b = b,a+b
    