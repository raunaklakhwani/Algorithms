import sys
from collections import defaultdict
N = input()
A = map(int, raw_input().split())
dp = [None]*N
for i in xrange(N):
    dp[i] = defaultdict(int)
dp[0][A[0]] = 1
for i in xrange(1, N):
    Sum = 0
    for j in xrange(i, -1, -1):
        Sum += A[j]
        if j > 0:
            for k in dp[j-1]:
                dp[i][Sum ^ k] += dp[j-1][k]
        else:
            dp[i][Sum] += 1
    print dp
print dp[-1][0]