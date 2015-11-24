#URL : http://www.spoj.com/problems/M3TILE/

f = [0] * 31
g = [0] * 31

f[0] = 1
f[1] = 0
g[1] = 1
g[2] = 0


for i in xrange(2,31):
    f[i] = 2 * g[i-1] + f[i-2]
    g[i] = f[i-1] + g[i-2]
    
    
while True:
    N = input()
    if N == -1:
        break
    print f[N]
    
 
    