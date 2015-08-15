from math import sqrt
maximum = 100001
cache = [None] * maximum
cache[0] = 0
cache[1] = 0


primes = [1] * maximum
primes[0] = 0
primes[1] = 0
x = []
for i in xrange(2,len(primes)):
    if primes[i] == 1:
        primes[i] = i
        x.append(i)
        cache[i] = 1
        for j in xrange(2*i,len(primes),i):
            primes[j] = 0



primes = x


def getSumOfDivisors(N):
    num = N
    if N >= maximum :
        return 0
    if cache[N] is None:
        i = 0
        s = 1
        l = []
        while N != 1:
            prime = primes[i]
            c = 0
            while N%prime == 0 and N!= 1:
                c += 1
                N = N / prime
            if c!= 0:
                l.append((prime,c))
            i += 1
        for p,a in l:
            s *= ((p ** (a+1) - 1)/(p - 1))
        #print l,s
        cache[num] = s - num
        return s - num
    else:
        return cache[N]

#print getSumOfDivisors(1)

for N in xrange(100000,100000-1000,-1):
    ans = 0
    
    for i in xrange(1,N+1):
        s = getSumOfDivisors(i)
        if i != s:
            x = getSumOfDivisors(s)
            if i == x:
                #print i,s
                ans += (i + s)
    print ans/2
           
            
