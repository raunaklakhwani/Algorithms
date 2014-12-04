import random
input = [21, 3, 2, 4, 5, 6, 7, 1, 8, 9, 50]
def swap(indexA, indexB):
    input[indexA], input[indexB] = input[indexB], input[indexA]
    
def partition(pivotIndex, start, end):
    if pivotIndex != start :
        swap(pivotIndex, start)
    
    pivot = input[start]
    i = start + 1
    for j in range(start + 1, end + 1) : 
        if input[j] < pivot :
            swap(i, j)
            i = i + 1
    
    swap(i - 1, start)
    return i - 1

def quickSort(start, end):
    if start < end :
        randomPivot = random.randint(start, end)
        p = partition(randomPivot, start, end)
        quickSort(start, p - 1)
        quickSort(p + 1, end)
        
def kthSmallestNumber(start, end, order):
    if start <= end :
        #print input
        randomPivot = random.randint(start, end)
        #print 'start = ',start,' end = ',end,' order = ',order
        #print 'randomPivot = ',randomPivot
        #print 'Element = ',input[randomPivot]
        p = partition(randomPivot, start, end)
        #print 'Updated Input = ',input
        #print 'return = ',p
        if p > start + order :
            return kthSmallestNumber(start, p - 1, order)
        elif p < start + order :
            #order + start - p - 1 really important
            return kthSmallestNumber(p + 1, end, order + start - p - 1)
        else :
            return input[p]


if __name__ == '__main__':
    #print input
    order = 5
    value = kthSmallestNumber(0, len(input) - 1, order - 1)
    print value
    #print 'rr'
    quickSort(0, len(input) - 1)
    print input
    print input[order - 1] == value
