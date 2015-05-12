'''
Project Euler #74: Digit factorial chains
URL : https://www.hackerrank.com/contests/projecteuler/challenges/euler074
'''

from collections import defaultdict
N,L = (221,7)
F = [1,1,2,6,24,120,720,5040,40320,362880 ,3628800]
cache = defaultdict(int)
def calcSum(n):
    s = 0
    if n == 0:
        return 1
    while (n!=0):
        d = n%10
        n = n/10
        s = s + F[d]
    return s

def nextTerm(N):
    l = [N]
    if cache.get(N) is None:
        while True:
            a = calcSum(N)
            #print a
            if cache.get(a) is None:
                try:
                    ind = l.index(a)
                    for index,v in enumerate(l):
                        if index > ind:
                            cache[v] = len(l) - ind
                        else:
                            cache[v] = len(l) - index
                    break
                except ValueError:
                    l.append(a)
                    N = a
            else:
                
                for index,v in enumerate(l):
                    cache[v] = len(l) - index + cache[a]
                    return
            

#print calcSum(720)
#nextTerm(3)

#print "hello"
for i in range(N):
    #print i
    nextTerm(i)
print cache
for key in sorted(cache.keys()):
    if cache[key] == L:
        print key
    
        
    
        
    
    