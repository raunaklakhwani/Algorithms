# URL : https://www.hackerrank.com/contests/countercode/challenges/campers

from math import ceil
N,K = 8,2
snipers = [2,6]
snipers.sort()




def getBetween(a,b):
    #print a,b
    n = b-a+1
    return int(ceil(n/2.0))

pre = 1
s = 0
for i in snipers:
    s += getBetween(pre, i - 2)
    #print s
    pre = i + 2
    
s += getBetween(pre, N)
    
print s + K
    
    
