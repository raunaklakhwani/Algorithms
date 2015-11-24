# URL : https://shanzi.gitbooks.io/algorithm-notes/content/problem_solutions/corn_fields.html

'''
2 3
1 1 1
0 1 0
'''

from math import log
N, M = map(int, raw_input().split())

def getResult(a, b):
    return (a ^ b) & ~a

farms = [0] * N
for i in xrange(N):
    p = map(int, raw_input().split())
    
    for j in xrange(len(p)):
        if p[j] == 1:
            farms[i] = farms[i] | (1 << j)
            
print farms

last = [0] * (1 << M)
curr = [0] * (1 << M)

last[0] = 1
for i in xrange(N):
    num = farms[i]
    ans = 0
    for j in xrange(1 << M):
        if last[j] == 0:
            continue
        
        for k in xrange(1 << M):
            if (j & k == 0) and (k & (k << 1) == 0):
                
                found = True
                x = k
                while x:
                    bit = x & ~(x - 1)
                    x = x & (x - 1)
                    if num & bit:
                        continue
                    else:
                        found = False
                        break
                if found:    
                    curr[k] += last[j]
                    ans += last[j]
                
    
    last = curr
    curr = [0] * (1 << M)
    
print ans
