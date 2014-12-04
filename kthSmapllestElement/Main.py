import random

input = [1000,23,43,56,76,5321, 3, 2, 4, 5, 1, 8, 9, 50,123,432,231]

def swap(input, indexA, indexB):
    input[indexA], input[indexB] = input[indexB], input[indexA]
    
def partition(input, pivotIndex, start, end):
    if pivotIndex != start :
        swap(input, pivotIndex, start)
    
    pivot = input[start]
    i = start + 1
    for j in range(start + 1, end + 1) : 
        if input[j] < pivot :
            swap(input, i, j)
            i = i + 1
    
    swap(input, i - 1, start)
    return i - 1

def quickSort(input, start, end):
    if start < end :
        randomPivot = random.randint(start, end)
        p = partition(input, randomPivot, start, end)
        quickSort(input, start, p - 1)
        quickSort(input, p + 1, end)
        
def kthSmallestNumber(input, start, end, order):
    '''
    Time complexity is O(n).
    Link : https://class.coursera.org/algo-004/lecture/36
    But it largely depends on pivot and in worst case, it could go to O(n^2)
    But in case you want that it should not approach worst case, you can use a smart method of medians of medians
    '''
    if start <= end :
        # print input
        randomPivot = random.randint(start, end)
        # print 'start = ',start,' end = ',end,' order = ',order
        # print 'randomPivot = ',randomPivot
        # print 'Element = ',input[randomPivot]
        p = partition(input, randomPivot, start, end)
        # print 'Updated Input = ',input
        # print 'return = ',p
        if p > start + order :
            return kthSmallestNumber(input, start, p - 1, order)
        elif p < start + order :
            # order + start - p - 1 really important
            return kthSmallestNumber(input, p + 1, end, order + start - p - 1)
        else :
            return input[p]
        
def kthSmalleshMethodSmartMethod(input,start, end, order) :
    '''
    Time Complexity : O(N)
    Link : https://class.coursera.org/algo-004/lecture/41, http://en.wikipedia.org/wiki/Median_of_medians#Algorithm
    Similar to kth smallestMethod. Only difference is that pivot element is not selected at random rather than its calculated
    from median of median logic
    '''
    if start <= end :
        pivotElement = calculateMedian(input,start,end)
        #This line is not useful if partition algorithm could be modified to directly pass the pivot element
        pivotIndex = input.index(pivotElement)
        p = partition(input, pivotIndex, start, end)
        if p > start + order :
            return kthSmalleshMethodSmartMethod(input, start, p - 1, order)
        elif p < start + order :
            # order + start - p - 1 really important
            return kthSmalleshMethodSmartMethod(input, p + 1, end, order + start - p - 1)
        else :
            return input[p]
    
def calculateMedian(input, start, end) :
    '''
    Recursively calculate the median of median from the input array
    Median of median is calculated by taking five elements at a time and then calculating the median by recursing
    The logic behind calculating median of median is it is guaranteed to have a good split of 30-70%
    Time Complexity : O(n)
    Space Complexity : O(n)
    '''
    size = 5
    length = end - start + 1
    num = length / size + 1
    
    if num <= 1 :
        return input[(start + end) / 2]
    else :
        while num > 1 :
            calc = []
            for i in range(num) :
                startIndex = start + i * 5
                endIndex = startIndex + 4 if len(input) > startIndex + 4 else len(input) - 1
                quickSort(input, startIndex, endIndex)
                calc.append(input[(startIndex + endIndex) / 2])
            length = len(calc)
            num = length / size + 1 
            input = calc
        startIndex = 0
        endIndex = len(input) - 1
        return input[(startIndex + endIndex) / 2]  
        
    


if __name__ == '__main__':
    # print input
    order = random.randint(0,len(input) - 1)
    value = kthSmallestNumber(input, 0, len(input) - 1, order - 1)
    print value
    # print 'rr'
    #quickSort(input, 1, 4)
    print input
    #quickSort(input, 0, len(input) - 1)
    print input
    print input[order - 1] == value
    print kthSmalleshMethodSmartMethod(input, 0, len(input) - 1, order - 1)
