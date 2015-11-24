#URL : https://shanzi.gitbooks.io/algorithm-notes/content/problem_solutions/arrange_the_bulls.html

'''
3 4
2 1 4
2 1 3
2 2 4
'''

from math import log
N,M = map(int,raw_input().split())

def getResult(a,b):
    return (a ^ b) & ~a

people = [0] * N
for i in xrange(N):
    p = map(int,raw_input().split())
    for j in xrange(1,len(p)):
        people[i] = people[i] | (1 << (p[j] - 1))
        
print people


last = [0] * (1<<M)
curr = [0] * (1<<M)
last[0] = 1

for i in xrange(N):
    num = people[i]
    ans = 0
    for j in xrange(1<<M):
        if last[j] == 0:
            continue
        
        mask = getResult(j, num)
        while mask:
            bitnum = int(log(mask & ~(mask - 1),2))
            curr[j | 1<<bitnum] += last[j]
            ans += last[j]
            mask = mask & (mask - 1)
    
    last = curr
    curr = [0] * (1<<M)
    print last
print ans
    
        
        
        
        
        
    
        
    
        
    
    