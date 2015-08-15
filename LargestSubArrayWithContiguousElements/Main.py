# URL : http://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/

def getLargestSubarrayWithContiguousElements(inp):
    '''
    >>> getLargestSubarrayWithContiguousElements([10,12,11])
    3
    
    >>> getLargestSubarrayWithContiguousElements([14, 12, 11, 20])
    2
    
    >>> getLargestSubarrayWithContiguousElements([1, 56, 58, 57, 90, 92, 94, 93, 91, 45] )
    5
    
    '''
    max_length = 1
    for start in xrange(0,len(inp) -1):
        minimum = maximum = inp[start]
        for end in xrange(start + 1,len(inp)):
            minimum = min(minimum,inp[end])
            maximum = max(maximum,inp[end])
            if maximum - minimum == end - start:
                max_length = max(max_length,end - start + 1)
    return max_length

if __name__ == '__main__':
    inp = [10,12,11]
    print getLargestSubarrayWithContiguousElements(inp)
    inp = [14, 12, 11, 20]
    print getLargestSubarrayWithContiguousElements(inp)
    inp = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45] 
    print getLargestSubarrayWithContiguousElements(inp)
    import doctest
    doctest.testmod()