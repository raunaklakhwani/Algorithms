# URL : http://www.spoj.com/problems/GNY07H/

N = 1002
x = [0] * N
a = [0] * N
b = [0] * N

x[0], x[1] = 1, 1
a[0], a[1] = 0, 1
b[0], b[1] = 0, 1

for i in xrange(2, N):
    x[i] = x[i - 1] + x[i - 2] + 2 * a[i - 1] + b[i - 1]
    a[i] = x[i - 1] + a[i - 1]
    b[i] = x[i - 1] + b[i - 2]
    
for i in xrange(input()):
    N = input()
    print (i + 1), x[N]
    
 
    
