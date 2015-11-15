from math import ceil, log

li = [[9, 18, 7, 13], [14, 3, 2, 10], [1, 8, 4, 9]]
seg = [float("-inf")] * ((4 ** (int(ceil(log(len(li) * len(li[0]), 4)) + 1))) - 1)


def buildSegmentTree(seg, index, a, b, c, d, li):
    print (a, b, c, d)
    if a == c and b == d:
        seg[index] = li[a][b]
    elif a > c or b > d:
        return 
    else:
        mid1 = (a + c) / 2
        mid2 = (b + d) / 2
        buildSegmentTree(seg, 4 * index + 1, a, b, mid1, mid2, li)
        buildSegmentTree(seg, 4 * index + 2, a, mid2 + 1, mid1, d, li)
        buildSegmentTree(seg, 4 * index + 3, mid1 + 1, b, c, mid2, li)
        buildSegmentTree(seg, 4 * index + 4, mid1 + 1, mid2 + 1, c, d, li)
        seg[index] = max(seg[4 * index + 1] , seg[4 * index + 2] , seg[4 * index + 3] , seg[4 * index + 4])
        
buildSegmentTree(seg, 0, 0, 0, len(li) - 1, len(li[0]) - 1, li)
        

print seg

def getMaximum(seg, index, qa, qb, qc, qd, a, b, c, d):
    if qa > c or qb > d or qc < a or qd < b or a > c or b > d:
        return float("-inf")
    elif a >= qa and b >= qb and c <= qc and d <= qd:
        return seg[index]
    else:
        mid1 = (a + c) / 2
        mid2 = (b + d) / 2
        m1 = getMaximum(seg, 4 * index + 1, qa, qb, qc, qd, a, b, mid1, mid2)
        m2 = getMaximum(seg, 4 * index + 2, qa, qb, qc, qd, a, mid2 + 1, mid1, d)
        m3 = getMaximum(seg, 4 * index + 3, qa, qb, qc, qd, mid1 + 1, b, c, mid2)
        m4 = getMaximum(seg, 4 * index + 4, qa, qb, qc, qd, mid1 + 1, mid2 + 1, c, d)
    
        return max(m1, m2, m3, m4)
    
print getMaximum(seg, 0, 1, 1, 2, 2, 0, 0, len(li) - 1, len(li[0]) - 1)
