from math import ceil,log
import sys

def getSegmentTreeUtil(inp, iStart, iEnd, segment, sIndex):
    if iStart != iEnd:
        mid = (iStart + iEnd) / 2
        left = getSegmentTreeUtil(inp, iStart, mid, segment, 2 * sIndex + 1)
        right = getSegmentTreeUtil(inp, mid + 1, iEnd, segment, 2 * sIndex + 2)
        segment[sIndex] = min(left, right)
    else:
        segment[sIndex] = inp[iStart]
    
    return segment[sIndex]

def getSegmentTree(inp):
    length = int(2 ** (ceil(log(len(inp), 2)) + 1) - 1)
    segment = [None] * length
    getSegmentTreeUtil(inp, 0, len(inp) - 1 , segment, 0)
    return segment


def getMinimumUtil(inp, seg, sStart, sEnd, iStart, iEnd, sI):
    if sStart <= iStart and sEnd >= iEnd:
        return seg[sI]
    elif sStart > iEnd or sEnd < iStart:
        return sys.maxint
    else:
        mid = (iStart + iEnd) / 2
        min1 = getMinimumUtil(inp, seg, sStart, sEnd, iStart, mid, 2 * sI + 1)
        min2 = getMinimumUtil(inp, seg, sStart, sEnd, mid + 1, iEnd, 2 * sI + 2)
        return min(min1, min2)
    

def getMinimum(inp, segmentTree, start, end):
    return getMinimumUtil(inp, segmentTree, start, end, 0, len(inp) - 1, 0)


def updateValueUtil(inp,seg,index,value,iStart,iEnd,nodeIndex):
    if index >= iStart and index <= iEnd:
        if iStart != iEnd:
            mid = (iStart + iEnd) / 2
            m1 = updateValueUtil(inp, seg, index, value, iStart, mid, 2 * nodeIndex + 1)
            m2 = updateValueUtil(inp, seg, index, value, mid + 1, iEnd, 2 * nodeIndex + 2)
            seg[nodeIndex] = min(m1,m2)
            return seg[nodeIndex]
        else:
            seg[nodeIndex] = value
            return seg[nodeIndex]
    else:
        return seg[nodeIndex] 
    

def updateValue(inp,seg,index,value):
    if index < 0 or index > len(inp) - 1:
        return
    inp[index] = value
    updateValueUtil(inp,seg,index,value,0,len(inp) - 1,0)
    
    
def getSegmentTreeUtil1(inp, iStart, iEnd, segment, sIndex):
    if iStart != iEnd:
        mid = (iStart + iEnd) / 2
        left = getSegmentTreeUtil1(inp, iStart, mid, segment, 2 * sIndex + 1)
        right = getSegmentTreeUtil1(inp, mid + 1, iEnd, segment, 2 * sIndex + 2)
        segment[sIndex] = max(left, right)
    else:
        segment[sIndex] = inp[iStart]
    
    return segment[sIndex]

def getSegmentTree1(inp):
    length = int(2 ** (ceil(log(len(inp), 2)) + 1) - 1)
    segment = [None] * length
    getSegmentTreeUtil1(inp, 0, len(inp) - 1 , segment, 0)
    return segment


def getMinimumUtil1(inp, seg, sStart, sEnd, iStart, iEnd, sI):
    if sStart <= iStart and sEnd >= iEnd:
        return seg[sI]
    elif sStart > iEnd or sEnd < iStart:
        return float("-inf")
    else:
        mid = (iStart + iEnd) / 2
        min1 = getMinimumUtil1(inp, seg, sStart, sEnd, iStart, mid, 2 * sI + 1)
        min2 = getMinimumUtil1(inp, seg, sStart, sEnd, mid + 1, iEnd, 2 * sI + 2)
        return max(min1, min2)
    

def getMinimum1(inp, segmentTree, start, end):
    return getMinimumUtil1(inp, segmentTree, start, end, 0, len(inp) - 1, 0)


def updateValueUtil1(inp,seg,index,value,iStart,iEnd,nodeIndex):
    if index >= iStart and index <= iEnd:
        if iStart != iEnd:
            mid = (iStart + iEnd) / 2
            m1 = updateValueUtil1(inp, seg, index, value, iStart, mid, 2 * nodeIndex + 1)
            m2 = updateValueUtil1(inp, seg, index, value, mid + 1, iEnd, 2 * nodeIndex + 2)
            seg[nodeIndex] = max(m1,m2)
            return seg[nodeIndex]
        else:
            seg[nodeIndex] = value
            return seg[nodeIndex]
    else:
        return seg[nodeIndex] 
    

def updateValue1(inp,seg,index,value):
    if index < 0 or index > len(inp) - 1:
        return
    inp[index] = value
    updateValueUtil1(inp,seg,index,value,0,len(inp) - 1,0)
    




        

def  maximum_minimum(arr, m):
    myMaximum(arr, m)
    m1 = maximum(arr, m, 0, {})
    print m1
    m2 = minimum(arr, m, 0, {})
    print m2
    
 

def getMaxMin(temp,temp1,i,j):
    
    m1 = float("-inf")
    m2 = float("inf")
    for k in xrange(i,j):
        m1 = max(m1,temp[k])
        m2 = min(m2,temp1[k])
        
    return m1,m2
        
    
    
            
    
        


def myMaximum(arr,m):
    N = len(arr)
    temp = [float("-inf")] * len(arr)
    temp[-1] = arr[-1] if arr[-1] > 0 else 0
    
    temp1 = [float("inf")] * len(arr)
    temp1[-1] = arr[-1] if arr[-1] < 0 else 0
    
    minSegmentTree = getSegmentTree(temp1)
    maxSegmentTree = getSegmentTree1(temp)
    
    
    
    for i in xrange(len(arr) - 2,-1,-1):
        
        
        inc = arr[i] + (temp[i + m + 1] if (i + m + 1) < N else 0)
        #exc = max(temp[i+1:i+m+1])
        exc = getMinimum1(temp, maxSegmentTree, i + 1, i + m)
        updateValue1(temp, maxSegmentTree, i, max(inc,exc))
        #temp[i] = max(inc,exc)
        
        inc1 = arr[i] + (temp1[i + m + 1] if (i + m + 1) < N else 0)
        #=======================================================================
        # exc1 = min(temp1[i+1:i+m+1])
        # temp1[i] = min(inc1,exc1)
        # 
        #=======================================================================
        exc = getMinimum(temp1, minSegmentTree, i + 1, i + m)
        updateValue(temp1, minSegmentTree, i, min(inc,exc))
        
    print temp,temp1
        
    return temp[0],temp[1]
        
        
        
    
    
     

def maximum(arr,m,index,cache):
    if cache.get(index) is not None:
        return cache[index]
    elif index >= len(arr):
        return 0
    else:
        x = maximum(arr,m,index + 1,cache)
        y = arr[index] + maximum(arr,m,index + m + 1,cache)
        cache[index] = max(x,y)
        return cache[index]
        
        
def minimum(arr,m,index,cache):
    if cache.get(index) is not None:
        return cache[index]
    elif index >= len(arr):
        return 0
    else:
        x = minimum(arr,m,index + 1,cache)
        y = arr[index] + maximum(arr,m,index + m + 1,cache)
        cache[index] = min(x,y)
        return cache[index]
        
    
    
    


if __name__ == '__main__':
    print
    
    
    #maximum_minimum([5, 8, 3, 1, 5, 7], 2)
    maximum_minimum([-1,-2,1,3,7], 1)
