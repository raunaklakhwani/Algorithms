#URL : https://shanzi.gitbooks.io/algorithm-notes/content/problem_solutions/frequent_values.html
'''
10 3
-1 -1 1 1 1 1 3 10 10 10
2 3
1 10
5 10
0
'''
from math import ceil, log

def buildSegmentTree(m, left, right, li, index, start, end):
    if start > end:
        return
    if start == end:
        m[index] = 1
        left[index] = 1
        right[index] = 1
        return
    
    mid = start + ((end - start) >> 1)
    cl = 2 * index + 1
    cr = 2 * index + 2
    buildSegmentTree(m, left, right, li, cl, start, mid)
    buildSegmentTree(m, left, right, li, cr, mid + 1, end)
    
    left[index] = left[cl]
    right[index] = right[cr]
    
    ans = 0
    if li[mid] == li[mid + 1]:
        ans = left[cr] + right[cl]
        if li[start] == li[mid + 1]:
            left[index] += left[cr]
        
        if li[mid] == li[end]:
            right[index] += right[cl]
    m[index] = max(m[cl], m[cr], ans)
    
def query(m, left, right, li, index, start, end, qs, qe):
    if start > end:
        return 0

    if qs <= start and qe >= end:
        return m[index]
    elif qs > end or qe < start:
        return 0
    else:
        ans = 0
        mid = start + ((end - start) >> 1)
        cl = 2 * index + 1
        cr = 2 * index + 2
        l = query(m, left, right, li, cl, start, mid, qs, qe)
        r = query(m, left, right, li, cr, mid + 1, end, qs, qe)
        
        if li[mid] == li[mid + 1]:
            ans = min(left[cr], qe - mid) + min(right[cl], mid - qs + 1)
        
        return max(l, r, ans)
    
    


def getAns(li, N, Q):
    l = ((2 ** int(ceil(log(N, 2)) + 1)) - 1)
    left = [0] * l
    right = [0] * l
    m = [0] * l
    
    buildSegmentTree(m, left, right, li, 0, 0, N - 1)
    #print m,left,right
    
    for q in Q:
        print query(m, left, right, li, 0, 0, N - 1, q[0] - 1, q[1] - 1)
    

while True:
    test = raw_input().split()
    if test[0] == "0":
        break
    N, Q = map(int, test)
    li = map(int, raw_input().split())
    q = []
    for _ in xrange(Q):
        q.append(map(int, raw_input().split()))
    
    getAns(li, N, q)
    
    
