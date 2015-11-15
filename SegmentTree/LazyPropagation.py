from math import ceil, log

def getSumUtil(li, seg, lazy, a, b, qs, qe, index):
    if lazy[index]:
        seg[index] += (lazy[index] * (qe - qs + 1))
        if qs != qe:
            lazy[2 * index + 1] = lazy[index]
            lazy[2 * index + 2] = lazy[index]
        lazy[index] = 0
    
        
    
    if b < qs or a > qe:
        return 0
    elif a == qs and b == qe:
        return seg[index]
    else:
        mid = (qs + qe) >> 1
        if a > mid:
            right = getSumUtil(li, seg, lazy, a, b, mid + 1, qe, 2 * index + 2)
            return right
        elif b <= mid:
            left = getSumUtil(li, seg, lazy, a, b, qs, mid, 2 * index + 1)
            return left
        else:
            left = getSumUtil(li, seg, lazy, a, mid, qs, mid, 2 * index + 1)
            right = getSumUtil(li, seg, lazy, mid + 1, b, mid + 1, qe, 2 * index + 2)
            return left + right

def getSum(li, seg, lazy, a, b):
    return getSumUtil(li, seg, lazy, a, b, 0, len(li) - 1, 0)

def updateSegmentTreeUtil(seg, qs, qe, index, diff, ind):
    if qe >= index and qs <= index:
        seg[ind] += diff
        if qs != qe:
            mid = (qs + qe) >> 1
            updateSegmentTreeUtil(seg, qs, mid, index, diff, 2 * ind + 1)
            updateSegmentTreeUtil(seg, mid + 1, qe, index, diff, 2 * ind + 2)
    
def updateValue(li, seg, index, value):
    diff = value - li[index] 
    li[index] = value
    updateSegmentTreeUtil(seg, 0, len(li) - 1, index, diff, 0)

def getSegmentTreeUtil(li, seg, lis, lie, ind):
    if lis == lie:
        seg[ind] = li[lis]
        return seg[ind]
    else:
        mid = (lis + lie) >> 1
        left = getSegmentTreeUtil(li, seg, lis, mid, 2 * ind + 1)
        right = getSegmentTreeUtil(li, seg, mid + 1, lie, 2 * ind + 2)
        seg[ind] = left + right
        return seg[ind]

def getSegmentTree(li):
    l = int(2 ** (ceil(log(len(li), 2)) + 1) - 1)
    seg = [0] * l
    getSegmentTreeUtil(li, seg, 0, len(li) - 1, 0)
    return seg

def updateRangeUtil(li, seg, lazy, a, b, qs, qe, index, inc):
    if a > qe or b < qs:
        return 
    elif a == qs and b == qe:
        if lazy[index]:
            seg[index] += (inc * (qe - qs + 1))
            
            if qs != qe:
                lazy[2 * index + 1] = lazy[index]
                lazy[2 * index + 2] = lazy[index]
            lazy[index] = 0
            
            
        
        if qs == qe:
            seg[index] += inc
        else:
            seg[index] += (inc * (qe - qs + 1))
            lazy[2 * index + 1] += inc
            lazy[2 * index + 2] += inc
    else:
        mid = (qs + qe) >> 1
        if a > mid:
            updateRangeUtil(li, seg, lazy, a, b, mid + 1, qe, 2 * index + 2, inc)
        elif b <= mid:
            updateRangeUtil(li, seg, lazy, a, b, qs, mid, 2 * index + 1, inc)
        else:
            updateRangeUtil(li, seg, lazy, mid + 1,b, mid + 1, qe, 2 * index + 2, inc)
            updateRangeUtil(li, seg, lazy, a, mid, qs, mid, 2 * index + 1, inc)
            
def updateRange(li, seg, lazy, a, b, inc):
    updateRangeUtil(li, seg, lazy, a, b, 0, len(li) - 1, 0, inc)
    
    

    
    
    
    
if __name__ == '__main__':
    inp = [5, 3, 7, 8, 9, 2]
    seg = getSegmentTree(inp)
    lazy = [0] * len(seg)
    #updateValue(inp, seg, 0, 10)
    print seg
    #print getSum(inp, seg, lazy, 0, 4)
    updateRange(inp, seg, lazy, 0, 4, 5)
    print seg
    print lazy
    print getSum(inp, seg, lazy, 1, 2)
    print seg,lazy
