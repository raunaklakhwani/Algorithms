# URL : http://www.geeksforgeeks.org/counting-inversions/
inp = [1, 20, 6, 4, 5]

#===============================================================================
# inp = [2, 1, 0, 2]
# inp = [2, 3, 1, 4]
#===============================================================================

def countMergeInversions(inp, start, mid, end):
    out = countInversion.out
    first = start
    second = mid + 1
    inv = 0
    index = start
    while first <= mid and second <= end:
        if inp[first] <= inp[second]:
            out[index] = inp[first]
            first += 1
        else:
            inv += (mid - first + 1)
            out[index] = inp[second]
            second += 1
        index += 1
        
    while first <= mid:
        out[index] = inp[first]
        first += 1
        
    while second <= end:
        out[index] = inp[second]
        second += 1
        
    for i in xrange(start, end + 1):
        inp[i] = out[i]
    
    return inv
        
    
        

def countInversionUtil(inp, start, end):
    if start >= end:
        return 0
    else:
        mid = start + (end - start) / 2
        a = countInversionUtil(inp, start, mid)
        b = countInversionUtil(inp, mid + 1, end)
        c = countMergeInversions(inp, start, mid, end)
        return a + b + c
    print

def countInversion(inp):
    if len(inp):
        countInversion.out = [0] * len(inp)
        x = countInversionUtil(inp, 0, len(inp) - 1)
        del countInversion.out
        return x
    else:
        return 0

if __name__ == '__main__':
    print countInversion(inp)
