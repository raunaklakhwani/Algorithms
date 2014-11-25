
import sys
import math
import copy

# input = [1,3,5,7,-2,-7,-9]
# input = [-1, -2, -3, -4, -5, 5]
#input = [1, 2, 4, 5, 7, -9]
input = [-1, 2, 4, 5, 7, 10]
K = 10

def bruteForceSumClosestToZero() :
    '''
    Time Complexity is O(n^2)
    '''
    minSum = sys.maxint
    source = ''
    destination = ''
    
    for i in range(0, len(input)) :
        s = input[i]
        for j in range(i + 1, len(input)) :
            d = input[j]
            difference = s + d
            if difference < K :
                difference = K - difference
            else :
                difference = difference - K
            if minSum > abs(difference) :
                minSum = abs(difference)
                source = s
                destination = d
    return [source, destination, minSum]

def smartClosestToZero() :
    '''
    Time Complexity is O(nlogn) because of sorting
    Logic is set a pointer to initial and end of the array as posIndex and negIndex
    calculate the sum at negIndex and posIndex
    Check the distance of the sum from K (note calculate the distance with sigh. i.e if its left to K it should be negative)
    if that distance > 0 then decrease posIndex else increase negIndex
    '''
    input1 = copy.deepcopy(input)
    input1.sort()
    minSum = sys.maxint
    source = ''
    destination = ''
    length = len(input1)
    negIndex = 0;
    posIndex = length - 1
    while negIndex < posIndex :
        s = input1[negIndex]
        d = input1[posIndex]
        difference = d + s
        #=======================================================================
        # if difference > K :
        #     difference1 = difference - K
        # else :
        #     difference1 = K - difference
        #=======================================================================
        difference1 = difference - K
        if minSum > abs(difference1) : 
            minSum = abs(difference1)
            source = s
            destination = d
        if difference1 < 0  :
            negIndex = negIndex + 1
        elif difference1 > 0 : 
            posIndex = posIndex - 1
        else :
            negIndex = negIndex + 1
            posIndex = posIndex - 1
              
                
        
    return [source, destination, minSum]
        


if __name__ == '__main__':
    print bruteForceSumClosestToZero()
    print smartClosestToZero()
