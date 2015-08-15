from math import log, ceil
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
    
    


if __name__ == '__main__':
    inp = [5, 3, 7, 8, 9, 2]
    seg = getSegmentTree(inp)
    print seg
    print getMinimum(inp, seg, 0, 5)
    updateValue(inp, seg, 2, -1)
    print seg
