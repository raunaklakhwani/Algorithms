'''
3
1 1 1 5
1
1
2 1 5 11
1 2
3 4
3 2 3 109
6 4 3
2 1 5

'''
from math import ceil, log

def buildSegmentTree(index, a, b, c, d, inp, N, K, C, X):
    # print (a, b, c, d)
    if a == c and b == d:
        seg[index] = ((A[a] * (a + 1)) % X + (B[b] * (b + 1)) % X + C % X) % X
    elif a > c or b > d:
        return 
    else:
        mid1 = (a + c) / 2
        mid2 = (b + d) / 2
        buildSegmentTree(4 * index + 1, a, b, mid1, mid2, inp, N, K, C, X)
        buildSegmentTree(4 * index + 2, a, mid2 + 1, mid1, d, inp, N, K, C, X)
        buildSegmentTree(4 * index + 3, mid1 + 1, b, c, mid2, inp, N, K, C, X)
        buildSegmentTree(4 * index + 4, mid1 + 1, mid2 + 1, c, d, inp, N, K, C, X)
        seg[index] = max(seg[4 * index + 1] , seg[4 * index + 2] , seg[4 * index + 3] , seg[4 * index + 4])
        

def getMaximum(index, qa, qb, qc, qd, a, b, c, d):
    print (index,qa,qb,qc,qd,a,b,c,d)
    
    if qa > c or qb > d or qc < a or qd < b or a > c or b > d:
        return float("-inf")
    elif a >= qa and b >= qb and c <= qc and d <= qd:
        return seg[index]
    else:
        mid1 = (a + c) / 2
        mid2 = (b + d) / 2
        m1 = getMaximum(4 * index + 1, qa, qb, qc, qd, a, b, mid1, mid2)
        m2 = getMaximum(4 * index + 2, qa, qb, qc, qd, a, mid2 + 1, mid1, d)
        m3 = getMaximum(4 * index + 3, qa, qb, qc, qd, mid1 + 1, b, c, mid2)
        m4 = getMaximum(4 * index + 4, qa, qb, qc, qd, mid1 + 1, mid2 + 1, c, d)
    
        return max(m1, m2, m3, m4)
    
     

seg = None
cache = None


with open("fourth.txt", "w+") as f:
    for t in xrange(input()):
        N, K, C, X = map(int, raw_input().split())
        A = map(int, raw_input().split())
        B = map(int, raw_input().split())
        
        #li = [[0] * (N) for i in xrange(N)]
        li = []
        #=======================================================================
        # for i in xrange(N):
        #     for j in xrange(N):
        #         li[i][j] = ((A[i] * (i + 1)) % X + (B[j] * (j + 1)) % X + C % X) % X
        #=======================================================================
                
        
        seg = [float("-inf")] * ((4 ** (int(ceil(log(N * N, 4)) + 1))) - 1)
        cache = {}
        print len(seg)
        if t == 24:
            print
        buildSegmentTree(0, 0, 0, N - 1, N - 1, li, N, K, C, X)
        s = 0
        # print seg
        for i in xrange(N - K + 1):
            for j in xrange(N - K + 1):
                #===============================================================
                # m = float("-inf")
                # # print (i,j),
                # for x in xrange(i, i + K):
                #     for y in xrange(j, j + K):
                #         m = max(m, li[x][y])
                # 
                # s += m
                #===============================================================
                m = getMaximum(0, i, j, i + K - 1, j + K - 1, 0, 0, N - 1, N - 1)
                # print (i, j, i + K - 1, j + K - 1), m
                s += m
                
            
        print s, t + 1
        f.write("Case #" + str(t + 1) + ": " + str(s) + "\n")
                    
