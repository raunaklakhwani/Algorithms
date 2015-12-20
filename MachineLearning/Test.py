'''
5
1 2 6 5 7

5
11 7 22 5 2
'''
from pprint import pprint
def getMinimumIndex(li, start, end):
    m = start
    for i in xrange(start, end + 1):
        if li[m] > li[i]:
            m = i
    return m


def getMaximumIndex(li, start, end):
    m = start
    for i in xrange(start, end + 1):
        if li[m] < li[i]:
            m = i
    return m


N = input()
li = map(int, raw_input().split())
dp = [[0] * N for _ in xrange(N)]


for l in xrange(2, N + 1):
    for i in xrange(N):
        start = i
        end = start + l - 1
        
        if end >= N:
            break
        
        m = getMinimumIndex(li, start, end)
        M = getMaximumIndex(li, start, end)
        
        first = (M - end) ** 2 + dp[start][end - 1]
        second = (m - start) ** 2 + dp[start + 1][end]
        
        dp[start][end] = min(first,second)
        
        
pprint(dp)



            
